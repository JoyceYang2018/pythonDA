# coding:utf-8


def gcd(m, n):
    while m%n != 0:
        m, n = n, m%n
    return n


def lcm(m, n):
    return m * n // gcd(m, n)


print(gcd(35, 14))
print(lcm(35, 14))
