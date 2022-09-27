#구현, 실버5, 방번호

n = input()
digitNum = [0 for i in range(9)]

for i in range(len(n)):
    if n[i] == '6' or n[i] == '9':
        digitNum[6] += 1
    else:
        digitNum[int(n[i])] += 1

if digitNum[6] % 2 == 0:
    digitNum[6] = digitNum[6] // 2
else:
    digitNum[6] = digitNum[6] // 2 + 1
print(max(digitNum))

