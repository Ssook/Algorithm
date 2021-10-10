# 출처 : https://www.acmicpc.net/problem/1966
from collections import deque
t = int(input())
for i in range(t):

    n, targetIndex = map(int, input().split())
    count = 1
    prior = deque(list(map(int, input().split())))
    indexes = deque(range(n))

    while(prior):
        cur = prior.popleft()
        index = indexes.popleft()
        if(prior and max(prior) > cur):
            prior.append(cur)
            indexes.append(index)
            count -= 1
        else:
            if(index == targetIndex):
                print(count)
        count += 1
