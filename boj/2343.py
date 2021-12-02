# 출처 : https://www.acmicpc.net/problem/2343
n, m = map(int, input().split())
lessons = list(map(int, input().split()))
answer = 20000000009


# limit크기를 최소라고 잡았을 때 블루레이 개수 구하는 함수
def check(limit):
    count = 0
    total = 0
    for i in range(n):
        if(total+lessons[i] > limit):
            count += 1
            total = lessons[i]
        else:
            total += lessons[i]

    if(total <= limit):
        return count+1
    else:
        return count+2


l = max(lessons)  # 가장 큰 강의가 최소값
r = 20000000009
# 이분 탐색
while(r >= l):
    mid = (r+l)//2
    if(check(mid) <= m):
        answer = min(answer, mid)
        r = mid - 1
    else:
        l = mid+1

print(answer)
