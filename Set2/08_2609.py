import sys

nList = list(map(int, sys.stdin.readline().split()))

nList.sort()
nList.reverse()
a, b = nList[0], nList[1]

while b > 0: # 최대 공약수, 유클리드 호제법
    a, b = b, a%b


print(a)
print(int(nList[0]*nList[1]/a))
