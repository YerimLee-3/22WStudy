import sys

n = int(sys.stdin.readline())
stk = []

for i in range(n):
    order = sys.stdin.readline().strip()
    
    if "push" in order:
        od = order.split()
        stk.append(int(od[1]))

    elif order == "pop":
        if len(stk) > 0:
            print(stk.pop())
        else:
            print(-1)

    elif order == "size":
        print(len(stk))

    elif order == "empty":
        if len(stk) > 0:
            print(0)
        else:
            print(1)

    elif order == "top":
        if len(stk) > 0:
            print(stk[len(stk)-1])
        else:
            print(-1)

