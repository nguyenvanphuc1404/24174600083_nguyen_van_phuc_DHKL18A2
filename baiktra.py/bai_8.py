# Nhập
chuyen_can = float(input ("Nhập điểm chuyên cần: "))
giua_ky = float (input( "Nhập điểm giữa kỳ: "))
cuoi_ky = float (input( "Nhập điểm cuối kỳ: "))

# Tính
diem_t_b = (chuyen_can + giua_ky + cuoi_ky) / 3

# xếp loại
if diem_t_b >= 9:
    diem = "A"
elif diem_t_b >= 7:
   diem = "B"

elif diem_t_b >= 5:
   diem = "C"
else:
   diem = "D"

# Kết quả
print( "Điểm trung bình:", round (diem_t_b, 3))
print("Xếp loại điểm:" , diem) 