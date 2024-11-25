# Nhập vào chuỗi ký tự
input_str = input("Nhập vào chuỗi ký tự: ")
# Khởi tạo các biến đếm
dem_chu = 0  
dem_so = 0   
dem_ky_tudacbiet = 0 
# kiểm tra từng ký tự trong chuỗi
for char in input_str:
    if char.isalpha(): 
        dem_chu += 1
    elif char.isdigit():  
        dem_so += 1
    else:  
        dem_ky_tudacbiet += 1
#  kết quả
print(f"Số ký tự là chữ: {dem_chu}")
print(f"Số ký tự là số: {dem_so}")
print(f"Số ký tự đặc biệt: {dem_ky_tudacbiet}")