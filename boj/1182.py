# 출처 : https://www.acmicpc.net/problem/1182
n, s = map(int, input().split())
numbers = list(map(int, input().split()))
global answer
answer = 0

# 백트래킹


def sol(index, sum):
    global answer
    if(index == n and sum == s):
        answer += 1
    if(index >= len(numbers)):
        return
    sol(index+1, sum)
    sol(index+1, sum+numbers[index])


sol(0, 0)
# 공집합 제외
if(s == 0):
    answer -= 1
print(answer)
