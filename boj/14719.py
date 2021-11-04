# 출처 : https://www.acmicpc.net/problem/14719
h, w = map(int, input().split())
graph = list(map(int, input().split()))
answer = 0

for i in range(1, w-1):
    height = graph[i]
    # 제일 높은 곳부터 높이마다 체크
    for j in range(h, height, -1):
        leftCheck = False
        rightCheck = False
        # 왼쪽 있는지 체크
        for k in range(0, i):
            if(graph[k] >= j):
                leftCheck = True
                break
        for a in range(i+1, w):
            if(graph[a] >= j):
                rightCheck = True
                break
        # 양쪽에 벽이 있다면 높이에서 아래 막혀있는 것 빼고 더함
        if(rightCheck and leftCheck):
            answer += j-height
            break

print(answer)
