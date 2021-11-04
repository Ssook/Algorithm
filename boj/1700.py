# 출처 : https://www.acmicpc.net/problem/1700
import heapq
n, k = map(int, input().split())
items = list(map(int, input().split()))
answer = 0
now = []
end = 0
for i in range(k):
    if(items[i] not in now):
        if(len(now) < n):
            now.append(items[i])
        else:
            end = i
            break
now = list(now)
# 멀티탭 개수가 충분할 때
if(end == k):
    print(0)
    exit(0)

# 나머지 사용해야 할 전기용품
rest = items[end:]
targets = []
for item in range(len(rest)):
    # 남은거 슬라이싱
    tempRest = rest[item:]
    if(rest[item] not in now):
        targets = []
        targetIndex = -1
        targetValue = -1
        # 만약 이번 아이템이 안 꽂혀있으면 가장 나중에 쓸 전기용품을 찾기 위해 현재 꽂혀있는 것들의 인덱스를 찾아줌
        for i in range(len(now)):
            if(now[i] in tempRest):
                thisIndex = tempRest.index(now[i])
                heapq.heappush(targets, (-1*thisIndex, now[i]))
            else:
                heapq.heappush(targets, (-999, now[i]))
        # 최대힙으로 가장 나중에 쓰는거 찾기
        t = heapq.heappop(targets)
        now.remove(t[1])
        now.append(rest[item])
        answer += 1
print(answer)
