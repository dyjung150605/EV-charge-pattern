# 1번 답안

# 음, 양의 정수를 각각 필터링해 모은 두 리스트를 합칩니다.
# 구글은 파이썬을 좋아하긴 하나 보네요.

# def do(alist):
#     return [x for x in alist if x < 0] + [x for x in alist if x >= 0]


# print(do([-1, 1, 3, -2, 2]))

# 근데 문제가 너무 간단한데 왠지 in-place로 풀어야하는 제약이 있는게 합당해보입니다.
# 그렇다고 하면 위에 이인욱님께서 푸신 방법이 맞습니다. (아마존 면접문제하고도 비슷하네요)

# 2번 답안
list1 = [-1, 1, 3, -2, 2]
print([i for i in list1 if i < 0] + [i for i in list1 if i > 0])
