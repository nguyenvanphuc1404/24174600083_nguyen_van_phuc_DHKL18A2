# Nhập 
loai_xe = float(input("Nhập loại xe (4 hoặc 7 chỗ): "))
so_km = float(input("Nhập số km đã đi: "))
thoi_gian_cho = float(input("Nhập thời gian chờ (phút): "))

# cước taxi
if loai_xe == 4:
    gia_mo_cua = 11000
    gia_trong_pham_vi = 12100
    gia_ngoai_pham_vi = 10000
    pham_vi = 20
elif loai_xe == 7:
    gia_mo_cua = 13000
    gia_trong_pham_vi = 14100
    gia_ngoai_pham_vi = 12000
    pham_vi = 30
else:
    print("Loại xe không hợp lệ, chỉ nhập 4 hoặc 7.")

# cước di chuyển
if so_km <= 0.8:
    di_chuyen = gia_mo_cua
elif so_km <= (0.8 + pham_vi):
    di_chuyen = gia_mo_cua + (so_km - 0.8) * gia_trong_pham_vi
else:
    di_chuyen = gia_mo_cua + pham_vi * gia_trong_pham_vi + (so_km - 0.8 - pham_vi) * gia_ngoai_pham_vi

# cước chờ
cho = 0
if thoi_gian_cho > 5:
    cho = (thoi_gian_cho - 5) * 800

# Tổng
tong = di_chuyen + cho

# In kết quả
print("số tiền phải trả là:", tong, "đồng")