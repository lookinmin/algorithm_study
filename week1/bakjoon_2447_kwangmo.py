n = int(input())

def makeStar(num):      #재귀함수
    arr = []
    if num == 1:
        return '*'
    star = makeStar(num // 3)       #재귀
    for i in star:
        arr.append(i * 3)           #[***]가 1개의 인덱스, n == 9면, [***] [***] [***]
    for i in star:
        arr.append(i + ' ' * (num // 3) + i)        #num에 따라 공백을 몇개 줄건지, 3=> 1번, 9 => 3번...
    for i in star:
        arr.append(i * 3)
    return arr


for i in makeStar(n):
    print(i)