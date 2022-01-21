import sys
# 시간 초과

def valid1(k):
    for i in range(k):
        if qColumn[k] == qColumn[i] or abs(qColumn[k]-qColumn[i]) == abs(k-i):
            return False
    
    return True

def dfs(c):
    global cnt

    if c == n:
        cnt += 1
        return

    for i in range(n):
        if visited[i]:
            continue

        qColumn[c] = i

        if valid1(c):
            visited[i] = True
            dfs(c+1)
            visited[i] = False

n = int(sys.stdin.readline())
qColumn = [0 for _ in range(n)]
visited = [False for _ in range(n)]
cnt = 0

dfs(0)
print(cnt)

