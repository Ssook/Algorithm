# 출처 : https://www.acmicpc.net/problem/2304
n = int(input())

cols = [list(map(int, input().split())) for _ in range(n)]

cols.sort(key=lambda x: (x[0]))

stack = []
for i in range(n):
    w = cols[i][0]
    h = cols[i][1]
    if(not stack):
        stack.append([w, h])
        continue

    if(stack[-1][1] <= h):
        stack.append([w, h])
    else:
        flag = True
        # 다음 기둥부터 끝까지 보면서 더 높은 게 없다면 스택에 넣어준다.
        for j in range(i, n):
            if(cols[j][1] > h):
                flag = False
                break

        if(flag):
            stack.append([w, h])

answer = 0


# 넓이 계산하는 부분
for i in range(len(stack)):
    w = stack[i][0]
    h = stack[i][1]

    # 다음 기둥이 있는 경우
    if(i+1 < len(stack)):
        nW = stack[i+1][0]
        nH = stack[i+1][1]
        # 다음 기둥의 높이가 현재 기둥보다 큰 경우
        if(nH >= h):
            answer += (nW-w)*h
        else:
            answer += ((nW-w)*nH+(h-nH))
    else:
        answer += h

print(answer)
