import sys
    

n = int(sys.stdin.readline())
nSet = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().split()))


for i in mList:
    if i in nSet:
        print(1, end=" ")
    else:
        print(0, end=" ")
        
    
