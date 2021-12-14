# 출처 : https://www.acmicpc.net/problem/2110
n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()

l = 1  # 최소 거리는 1
r = x[-1]-1  # 최대 거리는 가장 큰 x값에서 1 뺀 값


# distance만큼 거리를 띄우고 공유기를 설치했을 때 c개 안으로 사용할 수 있는지 체크하는 함수
def check(distance):
    start = x[0]
    count = 1
    # 집들마다 거리재고 설치해봄
    for i in range(1, n):
        if(x[i]-start >= distance):
            count += 1
            start = x[i]

    # 필요한 공유기 수가 더 많으므로 거리를 늘려서 공유기 갯수를 줄여야함
    if(count >= c):
        return True

    return False


answer = -1
# 이분탐색
while(r >= l):
    mid = (r+l)//2
    if(check(mid)):
        answer = mid
        l = mid+1
    else:
        r = mid - 1
print(answer)
