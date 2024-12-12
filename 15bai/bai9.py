

def simplify_fraction(numerator, denominator):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    common_gcd = gcd(numerator, denominator)
    return numerator // common_gcd, denominator // common_gcd
