import sys

def Lotto(start, depth):
    if depth == 6:
        print(" ".join(res[:6]))
        return 
    for i in range(start, k):
        res[depth] = sList[i]
        Lotto(i+1, depth+1)




while True:
    sList = list(map(str, sys.stdin.readline().split()))
    k = int(sList.pop(0))
    if k == 0:
        break
    res = [str(0)]*k
    Lotto(0,0)
    print()


    



