# 집합, 실버4, 나는야 포켓몬 마스터

from sys import stdin

n, m = map(int, stdin.readline().split())
pokedic_int_key = {}  # Key값이 int인 dictionary
pokedic_name_key = {}  # Key값이 str인 dictionary
for i in range(n):
    name = stdin.readline().strip()
    pokedic_int_key[i] = name
    pokedic_name_key[name] = i

# 포켓몬 탐색
for _ in range(m):
    item = stdin.readline().strip()
    # 입력값이 int일 경우, key값이 int인 dictionary에서 value를 가져옴
    if item.isdigit() == True:  # isdigit -> O(n)
        print(pokedic_int_key[int(item)-1])
    # 입력값이 int가 아닐 경우 (문자열일경우), key값이 str인 dictionary에서 value를 가져옴
    else:
        print(pokedic_name_key[item]+1)