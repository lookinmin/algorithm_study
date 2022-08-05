# 검증수, 브론즈5

a1, a2, a3, a4, a5 = map(int, input().split())

s = a1**2 + a2**2 + a3**2 + a4**2 + a5**2
print(s%10)