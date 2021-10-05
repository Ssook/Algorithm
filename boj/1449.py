# 출처 : https://www.acmicpc.net/problem/1449
n, l = map(int, input().split())
position = list(map(int, input().split()))

position.sort()

answer = 0
# 여러 지점의 차이가 l보다 작으면 한 테이프로 다 막을 수 있다.
while(position):
    now = position.pop(0)
    while(True and position):
        if(position[0]-now < l):
            position.pop(0)
        else:
            break
    answer += 1

print(answer)
