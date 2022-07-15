# 문자열, 브론즈3, 네 수
# 앞수 2개, 뒷 수 2개 더해서 문자열 합치기

n1, n2, n3, n4 = map(int, input().split())

str1 = str(n1)+str(n2)
str2 = str(n3)+str(n4)
print(int(str1) + int(str2))