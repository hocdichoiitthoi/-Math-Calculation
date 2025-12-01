import streamlit as st
import math

# Cấu hình tiêu đề trang web
st.set_page_config(page_title="Máy tính Casio Online", page_icon="🧮")

st.title("🧮 Máy tính Khoa học bằng Python")

# Tạo 2 cột để giao diện đẹp hơn
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Nhập số thứ nhất (a)", value=0.0)
with col2:
    num2 = st.number_input("Nhập số thứ hai (b)", value=0.0)

# Chọn phép tính
operation = st.selectbox(
    "Chọn phép toán",
    ("Cộng (+)", "Trừ (-)", "Nhân (*)", "Chia (/)", "Lũy thừa (a^b)", "Căn bậc 2 của a", "Sin(a)", "Cos(a)")
)

result = None

# Xử lý tính toán khi bấm nút
if st.button("Tính toán"):
    try:
        if operation == "Cộng (+)":
            result = num1 + num2
        elif operation == "Trừ (-)":
            result = num1 - num2
        elif operation == "Nhân (*)":
            result = num1 * num2
        elif operation == "Chia (/)":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Lỗi: Không thể chia cho 0")
        elif operation == "Lũy thừa (a^b)":
            result = math.pow(num1, num2)
        elif operation == "Căn bậc 2 của a":
            if num1 >= 0:
                result = math.sqrt(num1)
            else:
                st.error("Lỗi: Không thể tính căn bậc 2 của số âm")
        elif operation == "Sin(a)":
            # Chuyển đổi sang radian nếu cần, ở đây tính theo radian mặc định
            result = math.sin(num1)
        elif operation == "Cos(a)":
            result = math.cos(num1)
            
        # Hiển thị kết quả
        if result is not None:
            st.success(f"Kết quả: {result}")
            
    except Exception as e:
        st.error(f"Có lỗi xảy ra: {e}")

# Chạy thử dưới máy tính của bạn bằng lệnh: streamlit run app.py
