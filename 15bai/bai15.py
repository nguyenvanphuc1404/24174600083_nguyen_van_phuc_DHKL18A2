def is_perfect_number(n):
    if n <= 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
def smallest_perfect_number(numbers):
    # Lọc các số hoàn hảo trong dãy
    perfect_numbers = [num for num in numbers if is_perfect_number(num)]
    
    # Nếu có số hoàn hảo, trả về số nhỏ nhất
    if perfect_numbers:
        return min(perfect_numbers)
    else:
        return "Không có số hoàn hảo trong dãy"
