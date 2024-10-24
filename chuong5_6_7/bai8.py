import math # Bài 8


# Nhập giá trị x
x = float (input ("Nhập giá trị x: "))
# Kiểm tra điều kiện của x
if x > 0:
    # Phép tính
    log_4_x = math.log(x, 4)
    log_x_2 = math.log(2, x)
    # Tính toán
    dap_an = log_4_x + log_x_2
    dap_an = round (dap_an, 2)
    # Kết quả
    print ("Giá trị của biểu thức là:", dap_an) 
else:
    print( "Giá trị x phải lớn hơn 0 để thực hiện phép tính.")
