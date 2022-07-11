# 프로그램 실행 순서

# 입력할 정수의 개수를 사용자로부터 입력 받는다.
# 입력받은 정수의 개수만큼 정수를 입력받는다.
# 입력받은 정수의 합과 평균 값을 출력한다.
# 할당된 메모리공간을 비운다.
# 요구사항

# 메모리공간은 사용자의 입력 수의 따라 변동된다.
# 사용한 공간은 마지막에 비워야 한다.
# 배열을 사용하면 안된다.

n = int(input('정수의 개수를 입력하세요 : '))
sum_inputs = 0
for i in range(1, n+1):
    ith_value = int(input(f'{i}/{n}번째 숫자를 입력하세요 :'))
    sum_inputs += ith_value

print(f'합계 : {sum_inputs}')
print(f'평균 : {sum_inputs/n}')

del n, ith_value, sum_inputs
