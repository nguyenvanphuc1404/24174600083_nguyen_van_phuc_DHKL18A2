#bài 4
    #nhap thời gian
t_g = float(input("nhap thoi gian: "))
    #điêu kiện thời gian
if t_g > 0:
    # tri tiết bóng đèn
    h_d_t = 220
    cuong_do_dong_dien = 2.7
    cong_suat = 7000
    #phép tính
    cong_suat = t_g*h_d_t*cuong_do_dong_dien/ 3600*1000
    #tính
    phai_tra = cong_suat *7000
    # in kết quả
    print("tien phai tra la: ", phai_tra)
else:
    print("thoi gian su dang phan lon hon 0.") 