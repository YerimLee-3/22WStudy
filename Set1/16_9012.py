import sys

def findVPS(str1):
    flag = 0
    for a in str1:
        if a == '(':
            flag += 1
        elif a == ')':
            flag -= 1
        if flag < 0:
            return "NO"
    if flag > 0:
        return "NO"
    return "YES"

n = int(sys.stdin.readline())

for i in range(n):
    strVPS = str(sys.stdin.readline().strip())
    print(findVPS(strVPS))
