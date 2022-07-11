# 파이썬 eval(expression) 예제

# 1. 문자열 덧셈
a = eval('"BlockDMask" + "blog"')
print(f"1. eval('\"BlockDMask\"' + '\" blog\"') : {a}")

# 2. 숫자 덧셈
b = eval("100 + 32")
print(f'2. eval("100 + 32") : {b}')

# 3. 내장 함수 abs
c = eval("abs(-56)")
print(f'3. eval("abs(-56)") : {c}')

# 4. 리스트 길이
d = eval("len([1,2,3,4])")
print(f'4. eval("len([1,2,3,4])") : {d}')

# 5. round 함수
e = eval("round(1.5)")
print(f'5. eval("round(1.5)") : {e}')
