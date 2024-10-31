# Nhập tọa độ điểm m và tâm I
x, y = map(float, input("Nhập tọa độ của điểm M(x,y): ").split())
a, b = map(float, input("Nhập tọa độ của tâm I(a,b): ").split())
R = float(input("Nhập bán kính R: "))

# Tính khoảng cách 
k_c = ((x - a)**2 + (y - b)**2)**0.5

# Kiểm tra xem điểm M có nằm trong hoặc trên hình tròn không
if k_c <= R:
    print(True)
else:
    print(False)