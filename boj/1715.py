# 출처 : https://www.acmicpc.net/problem/1715
import heapq
cards = [int(input()) for _ in range(int(input()))]
cards.sort()
answer = 0
while(cards):
    if(len(cards) == 1):
        break
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    heapq.heappush(cards, a+b)
    answer += a+b

print(answer)
