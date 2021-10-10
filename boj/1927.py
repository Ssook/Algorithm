# 출처 : https://www.acmicpc.net/problem/1927
import heapq
import sys
l = []

n = int(input())
for i in range(n):
    x = int(sys.stdin.readline())
    if(x > 0):
        heapq.heappush(l, x)
    elif(x == 0):
        if(l):
            print(heapq.heappop(l))
        else:
            print(0)
