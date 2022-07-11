# 주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.

# 이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌

# 김씨와 이씨는 각각 몇 명 인가요?
# "이재영"이란 이름이 몇 번 반복되나요?
# 중복을 제거한 이름을 출력하세요.
# 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.

input_name = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
list_name = input_name.split(",")

# 김씨와 이씨는 각각 몇 명 인가요?
num_kim = 0
num_lee = 0

for i in list_name:
    if i[0] == "김":
        num_kim += 1
    elif i[0] == "이":
        num_lee += 1
    else:
        pass

print(f"김씨는 {num_kim}명입니다.")
print(f"이씨는 {num_lee}명입니다.")


# "이재영"이란 이름이 몇 번 반복되나요?
print()
num_iter = input_name.count('이재영')
print(f"이재영은 {num_iter}명입니다.")

# 중복을 제거한 이름을 출력하세요.
print()
list_deduplication = []
for i in list_name:
    if i not in list_deduplication:
        list_deduplication.append(i)

print(f"중복을 제거한 결과: \n{', '.join(list_deduplication)}")

# 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
print()
list_deduplication.sort()
print(f"중복을 제거하고 오름차순으로 정렬한 결과: \n{', '.join(list_deduplication)}")
