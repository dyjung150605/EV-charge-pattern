LIMIT = 4294967291  # 4294967291


def multiple(x, y):
    a, b, c, d = x
    i, j, k, l = y
#     return (a*i + b*k), (a*j+b*l), (c*i+d*k), (c*j+d*l)
    return (a*i + b*k) % LIMIT, (a*j+b*l) % LIMIT, (c*i+d*k) % LIMIT, (c*j+d*l) % LIMIT

# 추가   a b     i j
# 추가   c d     k l


def pow(x, n):
    if n == 0:
        return (1, 0, 0, 1)
    if n == 1:
        return x
    y = (1, 0, 0, 1)
    while n > 1:
        if n % 2 == 1:
            y = multiple(x, y)
            n = n - 1
        else:
            x = multiple(x, x)
            n = n // 2
    return multiple(x, y)


def fast_fib(n):
    if n == 1:
        return 0
    if n < 4:
        return 1
    a, b, c, d = pow((0, 1, 1, 1), n-3)
    return c + d


def do(n):
    return fast_fib(n) % 4294967291


# print(do(1000000000000000))
# print(do(10**100000))
# print(do(5))
print(multiple((1, 1, 1, 1), (1, 1, 1, 1)))
