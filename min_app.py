import streamlit as st
import time

st.set_page_config(page_title="Mô phỏng Thuật toán Tìm Min", layout="centered")

st.title("🔍 MÔ PHỎNG THUẬT TOÁN TÌM GIÁ TRỊ NHỎ NHẤT")

data = st.text_input("Nhập dãy số, cách nhau bởi dấu phẩy:", "5, 9, 2, 7, 1, 3")
arr = [int(x.strip()) for x in data.split(",") if x.strip()]

if st.button("▶️ Bắt đầu mô phỏng"):
    if not arr:
        st.error("Danh sách rỗng! Hãy nhập ít nhất 1 số.")
    else:
        min_val = arr[0]
        min_idx = 0
        
        st.write(f"Khởi tạo: min = {min_val} tại vị trí 0")

        bar = st.progress(0)
        steps = []

        for i in range(1, len(arr)):
            bar.progress(int((i / (len(arr)-1)) * 100))
            steps.append((i, arr[i], min_val))
            time.sleep(0.7)
            if arr[i] < min_val:
                min_val = arr[i]
                min_idx = i
                st.success(f"Cập nhật → min = {min_val} (vị trí {min_idx})")
            else:
                st.info("Không thay đổi")

        st.balloons()
        st.subheader(f"✅ KẾT QUẢ: min = **{min_val}** tại vị trí **{min_idx}**")
