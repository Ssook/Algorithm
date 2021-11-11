# 출처 : https://www.acmicpc.net/problem/12015
import bisect
n = int(input())
numbers = list(map(int, input().split()))


# lis
d = [numbers[0]]
for i in range(1, n):
    if(numbers[i] > d[-1]):
        d.append(numbers[i])
    else:
        # 이분탐색
        idx = bisect.bisect_left(d, numbers[i])
        d[idx] = numbers[i]


print(len(d))
