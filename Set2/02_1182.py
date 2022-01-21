import sys

def dfs(index, sum):
    global cnt
    
    if index >= n:    
        return 

    sum += nList[index]

    if sum == s:
        cnt += 1

    dfs(index+1, sum - nList[index]) # 선택하지 않은 경우
    dfs(index+1, sum) # 선택한 경우 


n, s = map(int, sys.stdin.readline().split())
nList = list(map(int, sys.stdin.readline().split()))

res = [0]*n
cnt = 0

dfs(0,0)
print(cnt)
