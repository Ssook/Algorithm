# 출처 : https://www.acmicpc.net/problem/2839
import math
n = int(input())
answer = 99999
# 5*i <= n 을 만족하는 최대값
maxFive = math.floor(n/5)
no = n

# 5를 한개 든 경우, 두개 든 경우... n 개 든 경우
for i in range(maxFive+1):
    no = n
    no = no - (5*i)
    if (no % 3 != 0):
        answer = min(99999, answer)
    else:
        answer = min(answer, i+(no//3))

if(answer == 99999):
    print(-1)
else:
    print(answer)
