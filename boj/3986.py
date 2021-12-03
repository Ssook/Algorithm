# 출처 : https://www.acmicpc.net/problem/3986
n = int(input())
word = [list(input()) for _ in range(n)]
answer = 0
for i in range(n):
    if(len(word[i]) % 2 == 0):
        stack = []
        thisWord = word[i]
        for j in range(len(thisWord)):
            if(not stack):
                stack.append(thisWord[j])
            else:
                if(stack[-1] == thisWord[j]):
                    stack.pop()
                else:
                    stack.append(thisWord[j])
        if(not stack):
            answer += 1

print(answer)
