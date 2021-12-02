# 출처 : https://www.acmicpc.net/problem/4889
answer = []
while(True):
    brace = list(input())
    if('-' in brace):
        break

    stack = []
    count = 0
    for i in range(len(brace)):
        if(brace[i] == '{'):
            stack.append('{')
        else:
            if(not stack):  # 닫는 괄호인데 스택이 비어있다면 { 로 바꾸어서 스택에 넣어준다.
                count += 1
                stack.append('{')
            else:
                # 닫는 괄호 차례에 스택의 top이 {인 경우 정상적인 동작
                if(stack[-1] == '{'):
                    stack.pop()

                # 스택의 top이 } 인 경우 {로 바꾸고 짝이 이루어졌다고 생각한다.
                else:
                    count += 1
                    stack.pop()

    # 스택에 남아있는 { 가 있다면 절반을 }로 바꾸면 성립
    if(stack):
        count += len(stack)//2
    answer.append(count)

for a in range(len(answer)):
    print(str(a+1)+'.', answer[a])
