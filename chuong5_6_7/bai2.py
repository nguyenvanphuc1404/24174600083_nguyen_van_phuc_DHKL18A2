# Bài 2
# Nhập x
x = float (input("Nhập giá trị của x: "))
# Kiểm tra điều kiện của x
if x > 0:
    # Phép tính
    tu_so = -x + (x**2 + 4)**(1/2)
    mau_so = ( x**4 + 1)**(1/7)
    f_x = tu_so / mau_so
    # Tính
    ket_qua = round (f_x, 3)
    # In kết quả
    print ("Giá trị của biểu thức là:", ket_qua)
else:
    print ("Giá trị x phải lớn hơn 0 để thực hiện phép tính.")