# 🌱 Potato Disease Classification & AI Assistant

Dự án ứng dụng Deep Learning để nhận diện bệnh trên lá khoai tây thông qua hình ảnh và tích hợp Trợ lý AI để tư vấn cách điều trị.

## 📂 Tổng quan
- **Frontend**: Django Templates, HTML5, Tailwind CSS (CDN), JavaScript.
- **Backend**: Django Framework (Python).
- **AI/DL**: TensorFlow/Keras (Dự kiến cho model nhận diện), API Chatbot.

## 🛠 Yêu cầu hệ thống
- Python 3.8 trở lên.
- Kết nối Internet (để tải Tailwind CSS từ CDN).

## 🚀 Hướng dẫn cài đặt

### 1. Thiết lập môi trường
Mở terminal tại thư mục gốc của dự án và chạy các lệnh sau:

```bash
# Tạo môi trường ảo (khuyên dùng)
python -m venv venv

# Kích hoạt môi trường ảo
# Trên Windows:
venv\Scripts\activate
# Trên macOS/Linux:
source venv/bin/activate
```

### 2. Cài đặt thư viện
```bash
pip install -r requirements.txt
```

## ⚙️ Cấu hình quan trọng

Trong file `templates/index.html`, hiện tại các API đang trỏ cứng đến địa chỉ IP `10.22.153.106`.

- Nếu bạn chạy local, hãy mở file `templates/index.html` và thay thế `http://10.22.153.106:8000` thành `http://127.0.0.1:8000` hoặc `http://localhost:8000`.
- Các dòng cần sửa nằm trong hàm `uploadImage()` và `sendMessage()`.

## ▶️ Chạy dự án

1. **Khởi động Server:**
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

2. **Sử dụng:**
   - Mở trình duyệt và truy cập: `http://localhost:8000` (hoặc IP máy chủ của bạn).
   - Upload ảnh lá khoai tây để nhận diện bệnh.
   - Chat với AI để nhận lời khuyên.