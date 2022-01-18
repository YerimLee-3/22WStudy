import sys

n = int(sys.stdin.readline())
nStack = []
res = []

flag = 0
temp = 1


for i in range(n):
    j = int(sys.stdin.readline())
    while temp <= j:
        nStack.append(temp)
        res.append("+")
        temp += 1
    if nStack[-1] == j:
        nStack.pop()
        res.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    print("\n".join(res))



