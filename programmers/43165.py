# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    answer = 0

    def dfs(level, sum, answer):
        if(level == len(numbers)):
            if(sum == target):
                answer += 1
            return answer
        dfs(level+1, sum+numbers[level], answer)
        dfs(level+1, sum-numbers[level], answer)

    answer = dfs(0, 0, answer)

    return answer
