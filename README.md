# python
# Ứng dụng Dự đoán Giá Vàng

Ứng dụng web được xây dựng bằng Streamlit để dự đoán giá vàng dựa trên ngày và giá mua hiện tại.

## Tính năng

- Dự đoán giá vàng dựa trên ngày và giá mua
- Giao diện web thân thiện với người dùng
- Hiển thị kết quả dự đoán rõ ràng

## Cài đặt

1. Clone repository:
```bash
git clone https://github.com/nguyen-hai-anh06/project.git
cd project
```

2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## Cách sử dụng

1. Chạy ứng dụng:
```bash
streamlit run main.py
```

2. Truy cập ứng dụng:
- Mở trình duyệt web
- Truy cập: http://localhost:8501

3. Sử dụng ứng dụng:
- Chọn ngày muốn dự đoán
- Nhập giá mua hiện tại
- Nhấn nút "Dự đoán" để xem kết quả

## Thư viện sử dụng

- streamlit==1.31.1
- pandas==2.2.0
- numpy==1.26.4
- scikit-learn==1.4.0
