# 피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?

# 피보나치 수열을 만든다

list_fibo = [1, 2]
num_last = 4000000
value_last = list_fibo[len(list_fibo)-1]

while value_last <= num_last:
    i = len(list_fibo)
    num_add = list_fibo[i-1] + list_fibo[i-2]
    list_fibo.append(num_add)
    value_last = list_fibo[len(list_fibo)-1]

del list_fibo[i]
print('4000000이하까지의 피보나치 수열')
print(list_fibo)
print()

list_fibo_even = []

for j in list_fibo:
    if j % 2 == 0:
        list_fibo_even.append(j)
    else:
        pass

print('4000000이하까지의 피보나치 수열 중 짝수 리스트')
print(list_fibo_even)
print()

print('4000000이하까지의 피보나치 수열 중 짝수 합계')
print(sum(list_fibo_even))
