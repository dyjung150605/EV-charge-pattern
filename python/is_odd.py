def is_odd(number):
    if number % 2 == 1:   # 2로 나누었을 때 나머지가 1이면 홀수이다.
        result = "odd"
    else:
        result = "even"
    return result


print(is_odd(3))
