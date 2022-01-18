import sys

# 시간 초과

t = int(sys.stdin.readline())

for i in range(t):
    pList = list(str(sys.stdin.readline().strip()))
    n = int(sys.stdin.readline())

    nList = list(map(str, sys.stdin.readline().strip().strip("[]").split(",")))

    flag = 1

    for k in pList:
        if k == "R":
            nList.reverse()
        elif k == "D":
            if len(nList)>0 and n != 0:
                del nList[0]
            else: 
                flag = 0
        

    if flag == 0:
        print("error")
    else:
        print("[",",".join(nList),"]", sep='')    
    
    

