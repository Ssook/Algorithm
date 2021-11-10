# 출처 : https://www.acmicpc.net/problem/1699
import math
n = int(input())
d = [0, 1, 2, 3]
for i in range(4, n+1):
    power = int(math.sqrt(i))
    target = []
    # 가장 가까운 제곱수를 구하고, 줄여나가면서 dp
    while(power > 0):
        if(power*power == i):
            target.append(1)
        else:
            target.append(1+d[i-power*power])
        power -= 1
    d.append(min(target))

print(d[n])
