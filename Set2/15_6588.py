from re import I
import sys

def prime_list(n):
    sieve = [True]*n
    m = int(n**0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return sieve 

def find_sum(n):
    global sList

    for i in range(3, n):
        if sList[i] == True:
            if sList[n-i] == True:
                print("%d = %d + %d" %(n, i, n-i))
                return 
        if i > n//2:
            print("Goldbach's conjecture is wrong.")
            return



input = sys.stdin.readline
sList = prime_list(1000000)


n=int(input())
if n != 0:
    find_sum(n)

while n != 0:
    n=int(input())
    find_sum(n)
