#bài 8
import math
x = input("nhap gia tri x: ")
x = float(x)
f_x = math.log(x, 4) + math.log(2, x)
print(f"Gia tri can tim f(x) = {f_x:.2f}")



#bài 1
r = float(input("nhap vap ban kinh: "))
h = float(input("nhap vao chieu cao: "))
pi = 3.14
dtxq = 2*pi*r*h
dttp = dtxq + 2*pi*r**2
print(f"dien tich xung quanh: {dtxq:.2f}")
print(f"dien tich toan phan: {dttp:>2f}")


#bài 2 
#tu so = -x + (x**2 + 4)**(1/2)
#mau so = (x**4 + 1)**(1/7)
#f_x = (-x + (x**2 + 4)**(1/2))/((x**4 + 1)**(1/7))
print(f"giá trị của f(x) = {f_x:.2f}")



#bài 4
t = int(input("nhap thoi gian su dung bong den (s): "))
hieu_dien_the = 228
cuong_do_dong_dien = 2.7
cong_suat = t*hieu_dien_the*cuong_do_dong_dien/360*1000
phai_tra = cong_suat*7000
print("tien ien phai tra: ", phai_tra)
