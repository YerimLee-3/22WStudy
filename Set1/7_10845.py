import sys

n = int(sys.stdin.readline())
que = []
s = 0

for i in range(n):
    order = sys.stdin.readline().strip()
    lenQue = len(que) - s
    
    if "push" in order:
        od = order.split()
        que.append(int(od[1]))

    elif order == "pop":
        if lenQue > 0:
            print(que[s])
            s += 1
        else:
            print(-1)

    elif order == "size":
        print(lenQue)

    elif order == "empty":
        if lenQue > 0:
            print(0)
        else:
            print(1)

    elif order == "front":
        if lenQue > 0:
            print(que[s])
        else:
            print(-1)

    elif order == "back":
        if lenQue > 0:
            print(que[len(que)-1])
        else:
            print(-1)
