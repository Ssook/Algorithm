# 출처 : https://www.acmicpc.net/problem/2512
n = int(input())
budgets = list(map(int, input().split()))
total = int(input())
answer = []

# 배정한 예산의 합이 총 예산보다 큰 지 확인


def check(budgets, maximum):
    cost = 0
    for budget in budgets:
        cost += (min(budget, maximum))

    return cost


# 주어진 예산으로 다 감당할 수 있을 경우
if(sum(budgets) <= total):
    answer.append(max(budgets))
# 감당할 수 없는 경우 상한액을 기준으로 이분탐색
else:
    l = 0
    r = max(budgets)
    while(r >= l):
        m = (r+l)//2
        if(check(budgets, m) <= total):
            answer.append(m)
            l = m+1
        else:
            r = m-1
print(max(answer))
