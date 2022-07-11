# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)

# print(result)


numbers = [1, 2, 3, 4, 5]
result = [odd*2 for odd in numbers if odd % 2 == 1]
print(result)
