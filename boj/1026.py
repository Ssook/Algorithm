# 출처 : https://www.acmicpc.net/problem/1026
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 가장 작은 값을 만들기 위해서는 가장 큰수를 가장 작은 수에 곱해야 하므로
# b는 내림 차순, a는 오름차순으로 정렬한다.ㄴ
a.sort()
b.sort(reverse=True)
answer = 0
for i in range(n):
    answer += a[i]*b[i]

print(answer)
