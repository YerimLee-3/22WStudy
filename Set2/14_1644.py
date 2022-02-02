import sys

# 에라토스테네스의 체로 소수 구현 (1<=n<=4000000)

def prime_list(n):
    sieve = [True]*n
    m = int(n**0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i,j in enumerate(sieve) if j == True and i >= 2]

n = int(sys.stdin.readline())
sList = prime_list(n+1)


s = 0
cur = 0
cnt = 0

for k in range(0, len(sList)):
    s = k 
    sum = 0
    for j in range(k, len(sList)):
        cur = j
        sum += sList[cur]
        if sum == n: 
            cnt += 1
        elif sum > n:
            break

print(cnt)



