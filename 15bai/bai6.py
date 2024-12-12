def is_perfect_number(n):
    if n <= 1:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n
