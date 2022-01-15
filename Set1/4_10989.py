import sys

n = int(sys.stdin.readline())
numList = [0]*10001 # 리스트 크기 지정하여 선언

for i in range(n):
    numList[int(sys.stdin.readline())]+=1

for i in range(10001):
    if numList[i] != 0:
        for k in range(numList[i]):
            print(i)

