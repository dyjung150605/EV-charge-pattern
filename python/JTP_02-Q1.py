hong = {'국어': 80}
hong['영어'] = 75
hong['수학'] = 55
b = 0
# print(hong.values())
for a in list(hong.values()):
    b = b + a
print(b/3)
