import sys

n = int(sys.stdin.readline())
numSet = set()

for i in range(0,n):
    k = int(sys.stdin.readline())
    numSet.add(str(k))

print("\n".join(sorted(numSet)))
      
for i in sorted(numSet):
    print(i)

