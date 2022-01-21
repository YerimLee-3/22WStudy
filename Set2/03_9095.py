import sys

input = sys.stdin.readline

def dfs(idx, sum):
    global cnt

    if sum == n:
        cnt += 1
        return
    elif sum >= n:
        return 

    dfs(idx+1, sum+1)
    dfs(idx+1, sum+2)
    dfs(idx+1, sum+3)

t = int(input())

for _ in range(t):
    n = int(input())

    cnt = 0
    dfs(0,0)

    print(cnt)
