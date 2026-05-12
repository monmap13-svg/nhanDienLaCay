from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
# pyrefly: ignore [missing-import]
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import tensorflow as tf
from PIL import Image
from pydantic import BaseModel, Field
import io
from dotenv import load_dotenv
import os

# Import thư viện SDK mới của Gemini
from google import genai

# --------------------- ENV & GEMINI SETUP ---------------------
load_dotenv()

# Khởi tạo client cho Gemini. 
# Thư viện google-genai sẽ tự động tìm GEMINI_API_KEY trong biến môi trường (.env)
client = genai.Client()


model = tf.keras.models.load_model("nhanDienLaSauBenh.h5",)
CLASS_NAMES = ["Early_Blight", "Late_Blight", "Healthy"]
# --------------------- Load Knowledge Base ---------------------
# Đọc trực tiếp nội dung file knowledge base một lần khi khởi động app
try:
    with open('knowledge_base.txt', 'r', encoding='utf-8') as f:
        KNOWLEDGE_BASE_CONTENT = f.read()
except FileNotFoundError:
    KNOWLEDGE_BASE_CONTENT = "Không tìm thấy dữ liệu cơ sở."

# --------------------- FastAPI App ---------------------
app = FastAPI(title="Potato Disease Detector & Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="templates"), name="static")

@app.get("/")
def read_index():
    return FileResponse("templates/index.html")

# --------------------- Image Preprocessing ---------------------
def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    img = img.resize((256, 256))
    img_array = np.array(img).astype('float32') 
    
    img_array = np.expand_dims(img_array, axis=0)

    return img_array

# --------------------- Prediction Endpoint ---------------------
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = preprocess_image(contents)
    
    preds = model.predict(img)
    print("Xác suất thô:", preds)
    pred_class = CLASS_NAMES[np.argmax(preds[0])]
    confidence = float(np.max(preds[0]))
    
    return JSONResponse({
        "class": pred_class,
        "confidence": round(confidence, 4)
    })

# --------------------- Chat Endpoint (Gemini API) ---------------------
class Query(BaseModel):
    q: str = Field(..., description="Câu hỏi của người dùng")

@app.post("/chat")
async def chat(query: Query):
    # Tạo prompt với ngữ cảnh tiếng Việt
    prompt = f"""
Bạn là một Trợ lý Nông nghiệp ảo chuyên nghiệp.
Nhiệm vụ của bạn là giải đáp các thắc mắc chuyên sâu của người dùng về nông nghiệp, chăm sóc cây trồng (đặc biệt là bệnh trên khoai tây). Bạn được cung cấp một Cơ sở tri thức (Context) nội bộ, nhưng cũng được phép sử dụng kiến thức chuyên môn rộng lớn của mình để hỗ trợ người dùng.

Cơ sở tri thức (Context):
{KNOWLEDGE_BASE_CONTENT}

Câu hỏi của người dùng:
{query.q}

Hướng dẫn trả lời:
1. Ưu tiên 1 (Sử dụng Context): Hãy tìm kiếm thông tin trong phần "Cơ sở tri thức (Context)" trước. Nếu có thông tin liên quan, hãy sử dụng nó làm nền tảng chính cho câu trả lời.
2. Ưu tiên 2 (Mở rộng kiến thức): Nếu Context KHÔNG CÓ thông tin để trả lời, hãy tự do sử dụng vốn kiến thức chuyên sâu và cập nhật nhất của bạn về nông nghiệp, sinh học thực vật và các loại thuốc bảo vệ thực vật để giải đáp một cách chính xác.
3. Hình thức: Trả lời trực tiếp vào trọng tâm, ngắn gọn, súc tích và thân thiện. Sử dụng danh sách (bullet points) để liệt kê các bước, nguyên nhân hoặc giải pháp cho dễ đọc.
4. Giới hạn an toàn: Nếu người dùng hỏi những vấn đề không liên quan đến nông nghiệp hoặc chăm sóc cây trồng (ví dụ: chính trị, giải trí, code web...), hãy từ chối một cách lịch sự và hướng họ quay lại chủ đề chính.
"""
    
    try:
        # Sử dụng SDK mới để gọi model. 
        # Ở đây mình dùng gemini-2.5-flash để cho tốc độ và hiệu suất tốt nhất
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        answer = response.text
    except Exception as e:
        answer = f"Đã xảy ra lỗi khi gọi Gemini API: {str(e)}"

    return JSONResponse({
        "query": query.q,
        "answer": answer
    })

# --------------------- Run App ---------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))