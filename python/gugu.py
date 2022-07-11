def gugu(x):
    result = []
    for i in range(1, 10):
        result.append(x*i)
    return result


dan = int(input("단수를 입력하세요 : "))
print(gugu(dan))
