def divisors(n):
    result = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            result.append(i)
    return result
