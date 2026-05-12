# 🌿 PlantDoc - Hệ thống nhận diện bệnh lá cây AI

**PlantDoc** là một ứng dụng web tích hợp Deep Learning và Generative AI (Google Gemini) để chẩn đoán các bệnh thường gặp trên lá cây (ví dụ: khoai tây). Dự án không chỉ đưa ra kết quả chẩn đoán bệnh từ hình ảnh mà còn tích hợp trợ lý AI chuyên nghiệp để hướng dẫn cách điều trị, phòng ngừa.

---

## 🚀 Tính năng nổi bật

- **📸 Nhận diện qua hình ảnh:** Phân tích ảnh lá cây để phát hiện các bệnh như Khỏe mạnh, Mốc sương đến sớm (Early Blight), Mốc sương đến muộn (Late Blight).
- **🤖 Trợ lý AI tích hợp (Gemini):** Đưa ra tư vấn chuyên sâu về liều lượng thuốc, cách xử lý dựa trên tình trạng bệnh vừa phát hiện.
- **🕒 Lưu trữ lịch sử:** Lưu lại lịch sử chẩn đoán cục bộ trên trình duyệt (không cần database rườm rà).
- **🎨 Giao diện thân thiện:** Thiết kế hướng tự nhiên, dễ sử dụng, tương thích mượt mà trên cả điện thoại và máy tính.

---

## 🛠️ Công nghệ sử dụng

- **Backend:** Python, FastAPI, Uvicorn
- **AI/Machine Learning:** TensorFlow (nhận diện ảnh), Google Gemini API (`google-genai`)
- **Frontend:** HTML5, Vanilla JavaScript, Tailwind CSS (CDN)

---

## 💻 Hướng dẫn Cài đặt & Chạy trên máy tính (Local)

### 1. Yêu cầu hệ thống
- **Python:** Khuyến nghị sử dụng **Python 3.12**.
- **Tài khoản Google:** Cần có API Key từ [Google AI Studio](https://aistudio.google.com/) để sử dụng Gemini.

### 2. Cài đặt chi tiết

**Bước 1: Clone dự án về máy**
```bash
git clone https://github.com/monmap13-svg/nhanDienLaCay.git
cd nhanDienLaCay
```

**Bước 2: (Tùy chọn) Tạo môi trường ảo ảo (Virtual Environment)**
Để tránh xung đột thư viện với các dự án khác, hãy tạo môi trường ảo:
```bash
# Đối với Windows
python -m venv venv
venv\Scripts\activate

# Đối với macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**Bước 3: Cài đặt thư viện**
```bash
pip install -r requirements.txt
```

**Bước 4: Cấu hình API Key**
Tạo một file có tên `.env` ngay trong thư mục gốc của dự án và dán API key của bạn vào:
```env
GEMINI_API_KEY=AIzaSy... (thay bằng key thật của bạn)
```

### 3. Chạy ứng dụng

Gõ lệnh sau vào Terminal:
```bash
uvicorn app:app --reload
```
*(Hoặc dùng lệnh `python app.py`)*

Mở trình duyệt và truy cập vào:
👉 **http://localhost:8000**

---

## ☁️ Hướng dẫn Deploy lên Render

Dự án đã được cấu hình sẵn để dễ dàng deploy lên [Render.com](https://render.com/).

1. Đẩy code lên kho lưu trữ GitHub của bạn.
2. Đăng nhập Render, chọn tạo mới **Web Service** và liên kết với kho lưu trữ GitHub.
3. Render sẽ tự động đọc file `render.yaml` và `runtime.txt` để cài đặt môi trường (Python 3.12, Gunicorn).
4. Tại mục **Environment Variables** trên Render, hãy thêm biến:
   - `GEMINI_API_KEY`: Dán mã API key của bạn vào.
   - *(Không cần thêm port, Render sẽ tự cấp port cho FastAPI).*
5. Nhấn **Deploy** và chờ khoảng 5 phút. 

---

## 📄 Cấu trúc thư mục

```text
nhanDienLaCay/
├── app.py                  # Mã nguồn chính của Web Server
├── requirements.txt        # Danh sách thư viện Python
├── nhanDienLaSauBenh.h5    # Model Deep Learning đã huấn luyện
├── knowledge_base.txt      # Cơ sở tri thức cho Gemini AI
├── runtime.txt             # Định nghĩa phiên bản Python cho Render
├── render.yaml             # Cấu hình tự động deploy Render
└── templates/
    ├── index.html          # File giao diện trang web
    └── plantdoc_logo.png   # Logo ứng dụng
```

---
*© 2026 PlantDoc - Developed by Shinji (monmap13).*
