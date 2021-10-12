# 출처 : https://www.acmicpc.net/problem/6603
import sys
from itertools import combinations
x = []
while(True):
    x.append(sys.stdin.readline())
    if(len(x[-1]) < 6):
        break
# 완전탐색
for i in range(len(x)-1):
    x[i] = list(map(int, x[i].split()))[1:]
    for p in combinations(x[i], 6):
        print(str(p)[1:-1].replace(',', ''))
    if(i != len(x)-2):
        print('')
