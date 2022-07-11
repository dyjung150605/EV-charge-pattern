# 제너레이트 함수 정의
def d_fn(n):
    result = n
    n_list = list(str(n))
    for n_i in n_list:
        result += int(n_i)
    return result

# 1~5000까지 제너레이트 결과값 리스트를 만들어둔다.
gen_result=[]
for i in range(1,5000):
    gen_result.append(d_fn(i))

# 1~5000까지 값들 중에 결과값 리스트에 없으면 셀프넘버에 등록한다.
self_number=[]
for i in range(1,5000):
    if gen_result.count(i) == 0:
        self_number.append(i)

# print(self_number)
print(sum(self_number))
