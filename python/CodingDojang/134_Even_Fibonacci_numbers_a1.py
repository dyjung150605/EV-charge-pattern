a, b = [0,1]
sum = 0
while b <= 8:
    a = a + b
    b, a = a, b
    if b % 2 == 0: sum += b
print(sum)