# 출처 : https://www.acmicpc.net/problem/2805
n, m = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)  # 이분 탐색의 최대 값은 나무의 최대 높이
answer = []


# 자른 나무의 길이가 m보다 큰지 확인하기 위한 함수
def check(h, trees):
    meter = 0
    for tree in trees:
        if(tree-h >= 0):
            meter += tree-h
    return meter


# 이분 탐색 과정
while(right >= left):
    mid = (left+right)//2
    if(check(mid, trees) >= m):
        answer.append(mid)
        left = mid+1
    else:
        right = mid-1

# 최대값을 출력
print(max(answer))
