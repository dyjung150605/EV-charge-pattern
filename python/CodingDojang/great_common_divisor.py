# 두 수를 입력받는 리스트 생성하기
input_list = list(map(int, input().split()))

# for 문을 사용하여 입력 받은 두 수 각각의 약수 구하기
for i in input_list:
    a = globals()['num_{}'.format(i)] = list()
    for j in range(i+1):
        try:
            if i/j - i//j == 0:
                a.append(j)

        except:
            pass
    print('num_{}: '.format(i), a)  # 입력받은 약수 출력

###실제 변수 리스트는 num_입력숫자1, num_입력숫자2 라는 이름의 변수에 저장되어있음을 유의##
