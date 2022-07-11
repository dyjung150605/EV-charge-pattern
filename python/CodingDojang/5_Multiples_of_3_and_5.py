# 10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
# 1000미만의 자연수에서 3,5의 배수의 총합을 구하라.

limit = 1000
sum_3_5 = 0

for i in range(1, limit):
    if i % 3 == 0:
        sum_3_5 += i
    elif i % 5 == 0:
        sum_3_5 += i
    else:
        pass

print(sum_3_5)
