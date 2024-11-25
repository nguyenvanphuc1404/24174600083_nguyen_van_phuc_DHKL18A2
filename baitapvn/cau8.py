# Nhập 
str_xua1 = input("Nhập vào  : ")
str_xua2 = input("Nhập vào  : ")

# Kiểm tra
if str_xua2 in str_xua1:
    print(f"'{str_xua2}' nằm trong '{str_xua1}'")
else:
    print(f"'{str_xua2}' không nằm trong '{str_xua1}'")
if str_xua1 in str_xua2:
    print(f"'{str_xua1}' nằm trong '{str_xua2}'")
else:
    print(f"'{str_xua1}' không nằm trong '{str_xua2}'")