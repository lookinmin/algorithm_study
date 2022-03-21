
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

n1, n2, n3 = map(int, input().split())

if n1 == n2 == n3:
    print(10000 + n1*1000)
elif n1 == n2:
    print(1000 + n1 * 100)
elif n2 == n3:
    print(1000 + n2 * 100)
elif n1 == n3:
    print(1000 + n3 * 100)
else :
    print(max(n1, n2, n3) * 100)
