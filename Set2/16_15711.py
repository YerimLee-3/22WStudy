import sys

def prime_list(n):
    sieve = [True]*n
    m = int(n**0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return sieve 

def find_two(n):
    global sList

    for j in range(2, n):
        if sList[j]:
            if sList[n-j]:
                print("YES")
                return
    
    print("NO")
    return 


input = sys.stdin.readline

max = 2*2*(10**12)
sList = prime_list(max)

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    find_two(a+b)