# Nhập điểm của sinh viên
diem = input("điểm của sinh viên (A, B, C, D, E, F): ").upper()

# Phân loại sinh viên dựa vào điểm
if diem == "A":
    phan_loai = "sinh viên xuất sắc"
elif diem == "B":
    phan_loai = "sinh viên loại giỏi"
elif diem == "C":
    phan_loai = "sinh viên loại khá"
elif diem == "D":
    phan_loai = "sinh viên loại trung bình"
elif diem == "E":
    phan_loai = "sinh viên loại yếu"
elif diem == "F":
    phan_loai = "sinh viên xếp loại kém"
else:
    phan_loai = "Điểm không hợp lệ"

# In kết quả phân loại
print("sinh viên là :", phan_loai)