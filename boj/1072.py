# 출처 : https://www.acmicpc.net/problem/1072
x, y = map(int, input().split())
z = int((y*100/x))

left = 0
right = 2000000001
answer = []
# 이분탐색
while(right >= left):
    mid = (right+left)//2
    # mid만큼을 분모분자에 더한 것이 z보다 커지는 경우
    if(int((((y+mid)*100)/(x+mid))) > z):
        answer.append(mid)
        right = mid-1
    else:
        left = mid+1

if(answer):
    print(min(answer))
else:
    print(-1)
