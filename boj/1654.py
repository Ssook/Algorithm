# 출처 : https://www.acmicpc.net/problem/1654
k, n = map(int, input().split())
rans = []
for i in range(k):
    rans.append(int(input()))
answer = 0

# length길이로 잘랐을 때의 선 갯수를 반환


def check(length):
    count = 0
    for ran in rans:
        count += ran//length
    return count


left = 1
right = max(rans)
# 이분 탐색
while(right >= left):
    mid = (right+left)//2
    if(check(mid) >= n):
        answer = max(answer, mid)
        left = mid+1
    else:
        right = mid-1
print(answer)
