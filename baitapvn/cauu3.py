# Nhập họ tên 
full_ten = input("Nhập vào họ tên đầy đủ: ")

# Tách họ tên 
ten_parts = full_ten.split()
# Lấy họ và tên
ho = ten_parts[0]
ten = ten_parts[-1]

# kết quả
print(f"Ho: {ho}, Ten: {ten}")