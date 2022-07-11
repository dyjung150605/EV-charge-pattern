# 6 6

#   0   1   2   3   4   5
#  19  20  21  22  23   6
#  18  31  32  33  24   7
#  17  30  35  34  25   8
#  16  29  28  27  26   9
#  15  14  13  12  11  10

# 올림 사용을 위한 math 모듈 import
import math

# 행 개수와 열 개수에 대한 사용자 입력을 받는다.
m, n = map(int, input().split())

# 채워질 최종 숫자를 구한다.
num_last = m * n - 1

# 회전수를 구한다. m,n 중 작은 값을 2로 나눈 뒤 올림값
num_totalround = math.ceil(min(m, n)/2)

# 최종 행렬의 각 행을 리스트 변수 'list_행번호' 이름으로 생성한다.
for i in range(1, m+1):
    a = globals()['list_{}'.format(i)] = list()
    for j in range(1, n+1):
        a.append('')

# 바깥에서 안쪽으로 회전하면서 리스트 변수의 값을 채운다.
i = 1  # 행번호
j = 1  # 열번호
num_cur = 0

for num_curround in range(1, num_totalround+1):
    # 오른쪽으로 진행하면서 조건에 맞으면 행과 열 위치의 값을 대체함
    while j <= n-num_curround+1 and num_cur <= num_last:
        exec('list_'+str(i)+'['+str(j-1)+']='+str(num_cur))
        num_cur += 1
        if j == n-num_curround+1:
            i += 1
            break
        else:
            j += 1
    # 아래쪽으로 진행하면서 조건에 맞으면 행과 열 위치의 값을 대체함
    while i <= m-num_curround+1 and num_cur <= num_last:
        exec('list_'+str(i)+'['+str(j-1)+']='+str(num_cur))
        num_cur += 1
        if i == m-num_curround+1:
            j += -1
            break
        else:
            i += 1
    # 왼쪽으로 진행하면서 조건에 맞으면 행과 열 위치의 값을 대체함
    while j >= num_curround and num_cur <= num_last:
        exec('list_'+str(i)+'['+str(j-1)+']='+str(num_cur))
        num_cur += 1
        if j == num_curround:
            i += -1
            break
        else:
            j += -1
    # 위쪽으로 진행하면서 조건에 맞으면 행과 열 위치의 값을 대체함
    while i >= num_curround+1 and num_cur <= num_last:
        exec('list_'+str(i)+'['+str(j-1)+']='+str(num_cur))
        num_cur += 1
        if i == num_curround+1:
            j += 1
            break
        else:
            i += -1

# 최종적으로 출력한다.
for i in range(1, m+1):
    list_cur = eval('list_'+str(i))
    for j in list_cur:
        print('{:6d}'.format(j), end=' ')
    print()
