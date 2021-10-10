# 출처 : https://www.acmicpc.net/problem/1316
n = int(input())

answer = []
for _ in range(n):
    word = input()
    stack = []
    flag = True
    # 문자를 스택에 넣고, 스택의 맨위값을 체크해서 품
    for s in word:
        if(s not in stack):
            stack.append(s)
        elif(s in stack and stack[-1] == s):
            stack.append(s)
        elif(s in stack and stack[-1] != s):
            answer.append(False)
            flag = False
            break
    if(flag):
        answer.append(True)

print(answer.count(True))
