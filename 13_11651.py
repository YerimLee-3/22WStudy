import sys

n = int(sys.stdin.readline())
dotList =[]

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    dotList.append([x,y])

dotList.sort(key=lambda x:(x[1], x[0]))

for i in dotList:
    print(i[0], i[1])
