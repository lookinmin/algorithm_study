# 문자열, 브론즈2 애너그램 만들기

from collections import Counter
a = Counter(input())
b = Counter(input())
print(sum((a-b).values()) + sum((b-a).values()))