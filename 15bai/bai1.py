def is_integer(s):
    try:
        int(s)  # Cố gắng chuyển chuỗi thành số nguyên
        return True  # Nếu chuyển đổi thành công, trả về True
    except ValueError:
        return False  # Nếu gặp lỗi (không phải số nguyên), trả về False

