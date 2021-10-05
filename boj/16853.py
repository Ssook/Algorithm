a, b = map(int, input().split())

answer = 0
while(b > a):
    # 짝수이면 나누기 2
    if(b % 2 == 0):
        b = b//2
        answer += 1
    # 홀수인 경우 맨 끝이 1일때와 1이 아닐 때로 분기
    else:
        # 맨 끝이 1이 아니면 어떤 방법으로도 만들 수 없으므로 -1
        if(str(b)[-1] != '1'):
            answer = -1
            break
        # 맨 끝이 1이라면 1을 제거한다.
        else:
            b = int(str(b)[0:len(str(b))-1])
            answer += 1

# 연산을 다 마치고 나서 값이 다르면 만들 수 없는 것이다.
if(b != a):
    print(-1)
else:
    print(answer+1)
