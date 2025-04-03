# Ứng dụng Dự đoán Giá Vàng

Ứng dụng web được xây dựng bằng Streamlit để dự đoán giá vàng dựa trên ngày và giá mua hiện tại.

## Tính năng

- Dự đoán giá vàng dựa trên ngày và giá mua
- Giao diện web thân thiện với người dùng
- Hiển thị kết quả dự đoán rõ ràng

## Yêu cầu hệ thống

- Python 3.8 trở lên
- Các thư viện trong file requirements.txt

## Hướng dẫn cài đặt

1. **Cài đặt Python** (nếu chưa có):
   - Tải Python từ: https://www.python.org/downloads/
   - Trong quá trình cài đặt, nhớ tích vào ô "Add Python to PATH"
   - Khởi động lại máy tính sau khi cài đặt

2. **Tải code về máy**:
   - Cách 1: Tải ZIP
     - Click nút "Code" màu xanh trên GitHub
     - Chọn "Download ZIP"
     - Giải nén file ZIP đã tải về
   
   - Cách 2: Dùng Git
     ```bash
     git clone https://github.com/nguyen-hai-anh06/project.git
     cd project
     ```

3. **Cài đặt các thư viện**:
   - Mở Command Prompt hoặc PowerShell
   - Di chuyển vào thư mục project:
     ```bash
     cd đường_dẫn_đến_thư_mục_project
     ```
   - Cài đặt các thư viện:
     ```bash
     pip install -r requirements.txt
     ```

## Cách sử dụng

1. **Chạy ứng dụng**:
   - Mở Command Prompt hoặc PowerShell
   - Di chuyển vào thư mục project
   - Chạy lệnh:
     ```bash
     streamlit run main.py
     ```

2. **Truy cập ứng dụng**:
   - Ứng dụng sẽ tự động mở trong trình duyệt
   - Hoặc mở trình duyệt và truy cập: http://localhost:8501

3. **Sử dụng ứng dụng**:
   - Chọn ngày muốn dự đoán
   - Nhập giá mua hiện tại (đơn vị: x1000đ/lượng)
   - Nhấn nút "Dự đoán" để xem kết quả

## Xử lý lỗi thường gặp

1. **Lỗi "python không được nhận diện"**:
   - Cài đặt lại Python
   - Đảm bảo đã tích vào "Add Python to PATH"
   - Khởi động lại máy tính

2. **Lỗi khi cài đặt thư viện**:
   - Chạy với quyền Administrator
   - Cập nhật pip: `python -m pip install --upgrade pip`

3. **Lỗi không tìm thấy file model**:
   - Kiểm tra các file model (best_model.pkl, scaler.pkl) đã có trong thư mục chưa

## Thư viện sử dụng

- streamlit==1.31.1
- pandas==2.2.0
- numpy==1.26.4
- scikit-learn==1.4.0

## Hỗ trợ

Nếu gặp vấn đề, vui lòng tạo issue trên GitHub hoặc liên hệ qua email.
