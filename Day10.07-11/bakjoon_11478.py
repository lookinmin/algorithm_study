# 집합, 실버3, 서로 다른 부분 문자열의 개수

S = input()
res = set()
for i in range(len(S)):
    for j in range(i, len(S)):
        temp = S[i:j+1]
        res.add(temp)
print(len(res))