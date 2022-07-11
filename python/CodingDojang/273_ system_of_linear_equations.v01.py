# 방정식의 계수를 입력받는다.
eq1 = list(map(int, input("첫번째 방정식의 계수를 '3 2 4' 형태로 입력하세요 : \n").split()))
eq2 = list(map(int, input("두번째 방정식의 계수를 '3 2 4' 형태로 입력하세요 : \n").split()))

# eq1[0] x  +   eq1[1] y  =  eq1[2]
# eq2[0] x  +   eq2[1] y  =  eq2[2]

y = (eq2[0]*eq1[2]-eq1[0]*eq2[2])/(eq2[0]*eq1[1]-eq1[0]*eq2[1])
x = (eq1[2]-eq1[1]*y)/eq1[0]
print(f'x = {x}\ny = {y}')
# if eq[0]
# eq1[0] * eq2[0]
