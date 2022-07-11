# list comprehension
# print(sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0]))

# set library
set3 = set(range(3, 1000, 3))
set5 = set(range(5, 1000, 5))

print(sum(set3 | set5))
