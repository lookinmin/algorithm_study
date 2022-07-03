# 그리디 알고리즘 실버2 잃어버린 괄호
# 식의 값 최소로 만들기
# +, - 밖에 없음
# 다시 풀기
# 55 - 50 + 40 - 30 + 20 => 55 - (50 + 40) - (30 + 20)

line = input().split("-")
num = []
for i in line:
    cnt = 0
    s = i.split("+")
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]

for i in range(1, len(num)):
    n -= num[i]

print(n)

