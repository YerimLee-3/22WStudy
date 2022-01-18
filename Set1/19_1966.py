import sys


n = int(sys.stdin.readline())

for i  in range(n):
    all, q = map(int, sys.stdin.readline().split())
    impList = list(map(int, sys.stdin.readline().split()))

    ind = list(range(len(impList)))
    ind[q] = 'target'

    ord = 0
    while True:
        if impList[0] == max(impList):
            ord += 1
            
            if ind[0] == 'target':
               print(ord)
               break
            else:
                impList.pop(0)
                ind.pop(0)
        else:
            impList.append(impList.pop(0))
            ind.append(ind.pop(0))


   


