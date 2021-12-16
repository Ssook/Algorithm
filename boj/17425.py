# 출처 : https://www.acmicpc.net/problem/17425
t = int(input())
limit = 1000001
g = [0 for _ in range(limit)]  # 누적합
f = [0 for i in range(limit)]  # n의 약수의 합
answer = []

# n은 n의 배수의 약수인 것을 이용
for x in range(1, limit):
    mul = 1
    # ex) x가 3이면 3,6,9,12,15.. 등의 약수이므로 f[3의배수]+=3
    while(x*mul < limit):
        f[x*mul] += x
        mul += 1
    # 누적합 계산
    g[x] = g[x-1]+f[x]

for _ in range(t):
    n = int(input())
    answer.append(g[n])

for a in answer:
    print(a)
