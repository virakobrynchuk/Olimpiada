from fractions import gcd

a, b = [int(i) for i in input().split()]


def lcm(a, b):
    return abs(a*b) // gcd(a, b)


print(lcm(a, b))

