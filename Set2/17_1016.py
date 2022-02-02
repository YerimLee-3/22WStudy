import sys
# 에라토스테네스의 체
def find_list(n):
    sieve = [True]*(n+1)

    for i in range(2, n+1):
        if sieve[i] == True:
            j = i**2
            while j <= n+1:
                sieve[j] = False
                j = j**2

    return sieve 

min, max = map(int, sys.stdin.readline().split())
cnt = 0

nList = [1 for i in range(max-min+1)]

i = 2
while i**2 <= max:
    mul = min // i**2
    while mul * (i**2) <= max:
        if mul * (i**2) - min >= 0 and mul * (i**2) - min <= max - min:
            nList[mul * (i**2) - min] = 0
        mul += 1
    i += 1

print(sum(nList))