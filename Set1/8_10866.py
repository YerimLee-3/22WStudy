import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque()
s = 0

for i in range(n):
    order = sys.stdin.readline().strip()
    od = order.split()
    
    if "push_front" in order:
        dq.appendleft(int(od[1]))

    elif "push_back" in order:
        dq.append(int(od[1]))

    elif order == "pop_front":
        if len(dq) > 0:
            print(dq.popleft())
        else:
            print(-1)
    elif order == "pop_back":
        if len(dq) > 0:
            print(dq.pop())
        else:
            print(-1)

    elif order == "size":
        print(len(dq))

    elif order == "empty":
        if len(dq) > 0:
            print(0)
        else:
            print(1)

    elif order == "front":
        if len(dq) > 0:
            print(dq[0])
        else:
            print(-1)

    elif order == "back":
        if len(dq) > 0:
            print(dq[-1])
        else:
            print(-1)
