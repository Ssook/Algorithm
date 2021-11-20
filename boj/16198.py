# 출처 : https://www.acmicpc.net/problem/16198
import sys
sys.setrecursionlimit(100000)
n = int(input())
numbers = list(map(int, input().split()))
global answer
answer = 0


def recur(total):
    global answer

    if(total > answer):
        answer = total

    # 백트래킹
    # 첫번째 거와 마지막거를 제외하고 반복
    for i in range(1, len(numbers)-1):
        # i번째거 삭제하고 양 옆의 점수 곱해서 더함
        score = numbers[i-1]*numbers[i+1]
        total += score
        # 해당 숫자가 삭제되었다고 가정하고 다음 재귀
        delNumber = numbers[i]
        del numbers[i]
        recur(total)
        # 원상 복구
        total -= score
        numbers.insert(i, delNumber)


recur(0)

print(answer)
