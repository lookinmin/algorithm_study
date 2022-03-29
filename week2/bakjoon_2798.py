#브루트 포스-블랙잭 / 브론즈2

n, m = map(int, input().split())
card = list(map(int, input().split()))


sum = []            #카드 수의 합이 들어갈 list
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum.append(card[i] + card[j] + card[k]) #카드 수를 모두 더하면서 값을 sum에 담고

result = []         #최종 결과를 찾기위한 list
for i in sum:
    if i <= m:
        result.append(i)    # sum의 index중 m보다 크지 않으면 result에 담음
    else:
        continue

print(max(result))          # result의 index중 가장 큰 수 출력




