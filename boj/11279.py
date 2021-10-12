# 출처 : https://www.acmicpc.net/problem/11279
import heapq
import sys

n = int(sys.stdin.readline())
queue = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        # 최대 힙이므로 값을 음수로 바꾸어 큐에 삽입한다.
        heapq.heappush(queue, -x)
    else:
        if(queue):
            print(heapq.heappop(queue)*-1)
        else:
            print(0)
