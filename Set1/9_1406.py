import sys

st = sys.stdin.readline().strip()
strList = list(st)

strLeft = strList
strRight = []

m = int(sys.stdin.readline())

for i in range(m):
    order = sys.stdin.readline().strip().split()

    if order[0] == "L": 
        if strLeft != []:
            strRight.append(strLeft.pop())
            
    elif order[0] == "D":
        if strRight != []:
            strLeft.append(strRight.pop())

    elif order[0] == "B":
        if strLeft != []:
            strLeft.pop()

    elif order[0] == "P":
        strLeft.append(order[1])

print("".join(strLeft+list(reversed(strRight))))

# 시간 초과
'''
cur = len(strList)

for i in range(m):
    order = sys.stdin.readline().strip().split()

    if order[0] == "L": 
        if cur != 0:
            cur -= 1
            
    elif order[0] == "D":
        if cur != len(strList):
            cur += 1

    elif order[0] == "B":
        if cur != 0:
            strList = strList[:cur-1] + strList[cur:]
            cur -= 1

    elif order[0] == "P":
        strList = strList[:cur] + list(order[1]) + strList[cur:]
        cur += 1

print("".join(strList))
'''




