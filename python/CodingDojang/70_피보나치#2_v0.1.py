# 피보나치 수열이란, 첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때, 이후의 항들은 이전의 두 항을 더한 값으로 이루어지는 수열을 말한다. 예) 0, 1, 1, 2, 3, 5, 8, 13
# 피보나치 수열의 n번째 수를 4,294,967,291으로 나누었을 때의 나머지를 출력하는 프로그램을 작성하시오.

# 정수 n이 입력으로 주어진다. (1 <= n <= 10^100000)

# Sample input
# 5

# Sample output
# 3

# Sample input #2
# 1000000000000000

# Sample output #2
# 3010145777

n = int(input("1과 10^100000 사이의 정수 n을 입력하세요 : "))
seq_fibo = [0, 1]
a, b = seq_fibo
i = len(seq_fibo)

# num_nth = seq_fibo[n-1] #n번째 수

# if n<=2:
#     num_nth = seq_fibo[n-1] #n번째 수
# else:
while i < n:
    a += b
    a, b = b, a
    seq_fibo.append(b)
    i += 1
num_nth = seq_fibo[n-1]  # n번째 수

print(num_nth % 4294967291)
