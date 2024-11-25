#nhap
chuoi_tp = input("Nhập chuỗi bạn muốn kiểm tra :")
#kiểm tra và kết quả
if chuoi_tp.count('.') == 1 and chuoi_tp.replace('.','').isdigit():
    print("Đây là số thập phân ")
else :
    print("Đây ko phải số thập phân ")