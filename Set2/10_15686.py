from itertools import combinations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
chicken = []
possible_chicken = []
house = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i,j])
        if city[i][j] == 2:
            chicken.append([i, j])

for chk in list(combinations(chicken, m)):
    possible_chicken.append(chk)

min_chicken = 100000
for chk in possible_chicken:
    chk_sum = 0
    for k in house:
        i = k[0]
        j = k[1]

        find_min = 10000
        for q in chk:
            print(q[0], q[1])
            find_min = min(find_min, abs(i-q[0]) + abs(j-q[1]))
        
        chk_sum += find_min
    
    min_chicken = min(min_chicken, chk_sum)


print(min_chicken)
        
