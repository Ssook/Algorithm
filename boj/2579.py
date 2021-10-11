# 출처 : https://www.acmicpc.net/problem/2579
n = int(input())
stairs = []
d = []
for i in range(n):
    stairs.append(int(input()))
# 계단이 한 칸인 경우
if(n == 1):
    print(stairs[0])
else:
    d.append(0)
    d.append(stairs[0])
    d.append(stairs[0]+stairs[1])
    # 점화식
    for i in range(3, n+1):
        d.append(max(d[i-2]+stairs[i-1], d[i-3]+stairs[i-2]+stairs[i-1]))

    print(d[n])
