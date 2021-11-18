# 출처 : https://www.acmicpc.net/problem/2504
import copy
inputs = list(input())

global answer
answer = 0

# 올바른지 체크하는 함수


def check(stack):
    if(len(stack) % 2 == 1 or stack[-1] == '(' or stack[-1] == '['):
        return False
    else:
        checkStack = []
        for i in range(len(stack)):
            if(stack[i] == '('):
                checkStack.append('(')
            if(stack[i] == '['):
                checkStack.append('[')
            if(stack[i] == ')'):
                if(not checkStack):
                    return False
                if(checkStack[-1] != '('):
                    return False
                checkStack.pop()
            if(stack[i] == ']'):
                if(not checkStack):
                    return False
                if(checkStack[-1] != '['):
                    return False
                checkStack.pop()
    if(not checkStack):
        return True
    else:
        return False


# 재귀로 풀이
def recur(mul, braces):
    if(braces == []):
        global answer
        answer += mul
    stack = []
    for i in range(len(braces)):
        stack.append(braces[i])

        copyStack = copy.deepcopy(stack)
        # 올바른 괄호일 경우 재귀
        if(check(copyStack)):
            if(copyStack[0] == '['):
                recur(3*mul, copyStack[1:-1])
            if(copyStack[0] == '('):
                recur(2*mul, copyStack[1:-1])
            stack = []

    if(stack):
        print(0)
        exit(0)


recur(1, inputs)

print(answer)
