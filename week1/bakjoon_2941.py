# 알파벳 찾기, 실버5

str = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia :
    str = str.replace(i, '*')

print(len(str))
