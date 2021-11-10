# 출처 : https://www.acmicpc.net/problem/14501
# 완전 탐색
n = int(input())
time = []
profit = []
for i in range(n):
    t, p = map(int, input().split())
    time.append(t)
    profit.append(p)

answer = set([])

# 재귀적으로 완전탐색


def recur(index,  total):
    if(index > n):
        return
    answer.add(total)
    if(index == n):
        return
    recur(index+1, total)  # index번째 작업을 안하고 넘어감
    recur(index+time[index], total+profit[index])  # index번째 작업을 진행함


recur(0, 0)
print(max(answer))
