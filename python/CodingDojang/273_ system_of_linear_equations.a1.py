from math import lcm
from fractions import Fraction as frac  # 해를 float형이 아닌 분수 꼴로 나타내기 위해서

e1 = list(map(int, input().split()))  # 첫 번째 방정식
e2 = list(map(int, input().split()))  # 두 번째 방정식
A, B, C = e1
a, b, c = e2  # 계수들을 따로 뽑음

if (A*b == a*B):  # 해가 하나가 아닌 경우
    if (A*c == a*C):  # 해가 무수히 많은 경우
        print('해가 무수히 많습니다.')
    else:  # 해가 없는 경우
        print('해가 없습니다.')
else:
    l = lcm(B, b)
    f1 = int(l/B)
    f2 = int(l/b)
    for i in range(3):  # y의 계수를 맞추는 과정(가감법)
        e1[i] *= f1
        e2[i] *= f2
    e3 = []
    for j in range(3):  # y를 소거하고 x만 남기는 과정
        e3.append(e1[j]-e2[j])
    x = frac(e3[2], e3[0])  # x의 값
    y = (-A*x - C)/B  # 구한 x의 값을 첫 번째 방정식에 대입하여 y을 구하는 과정
    print('x =', x, 'y =', y)
