# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    answer = []

    def dfs(level, sum, answer):
        if(level == len(numbers)):
            if(sum == target):
                answer.append(1)
            return

        dfs(level+1, sum+numbers[level], answer)
        dfs(level+1, sum-numbers[level], answer)

    dfs(0, 0, answer)

    return len(answer)
