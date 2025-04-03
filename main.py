import pickle
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import os

def load_model(file_path):
    try:
        # Lấy đường dẫn tương đối từ thư mục hiện tại của file main.py
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, file_path)
        
        with open(full_path, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        st.error(f"Không tìm thấy file {file_path}")
        return None
    except Exception as e:
        st.error(f"Lỗi khi load model: {str(e)}")
        return None

# Load models
best_model = load_model('best_model.pkl')
scaler = load_model('scaler.pkl')

if best_model is None or scaler is None:
    st.error("Không thể khởi tạo ứng dụng. Vui lòng kiểm tra các file model.")
    st.stop()

def predict_price(date, price):
    try:
        # Tạo DataFrame với dữ liệu đầu vào
        x_df = pd.DataFrame([[date, price]], columns=["Date", "Buy Price (x1000đ/lượng)"])
        
        # Chuyển đổi ngày tháng
        x_df['Date'] = pd.to_datetime(x_df['Date'])
        x_df['year'] = x_df['Date'].dt.year
        x_df['month'] = x_df['Date'].dt.month
        x_df['day'] = x_df['Date'].dt.day
        x_df['dayofweek'] = x_df['Date'].dt.dayofweek
        
        # Chọn các cột cần thiết
        x_df = x_df[["year", "month", "day", "dayofweek", "Buy Price (x1000đ/lượng)"]]
        
        # Chuẩn hóa dữ liệu và dự đoán
        x_scaled = scaler.transform(x_df)
        y_pred = best_model.predict(x_scaled)
        
        return float(y_pred[0])
    except Exception as e:
        st.error(f"Lỗi khi dự đoán: {str(e)}")
        return None

# Giao diện người dùng
st.title("Dự đoán giá vàng")
st.write("Ứng dụng này giúp bạn dự đoán giá vàng dựa trên ngày và giá mua hiện tại.")

# Nhập liệu
date_input = st.date_input("Chọn ngày:", datetime.today())
price_input = st.number_input("Nhập giá mua (x1000đ/lượng):", min_value=0.0, step=0.01)

if st.button("Dự đoán"):
    if price_input <= 0:
        st.warning("Vui lòng nhập giá mua lớn hơn 0")
    else:
        prediction = predict_price(date_input, price_input)
        if prediction is not None:
            st.write(f"Giá dự đoán: {prediction:.3f} x1000đ/lượng")
            st.success("Dự đoán hoàn tất!")