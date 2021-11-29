# 출처 : https://www.acmicpc.net/problem/10844
n = int(input())
d = [[0 for i in range(10)] for j in range(101)]
d[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# d[i][j] 끝자리가 j 인 i자리 수
for i in range(2, n+1):
    for a in range(10):
        if(a == 0):
            d[i][a] = d[i-1][1] % 1000000000
        elif(a == 9):
            d[i][a] = d[i-1][8] % 1000000000
        else:
            d[i][a] += d[i-1][a-1] % 1000000000+d[i-1][a+1] % 1000000000

print(sum(d[n]) % 1000000000)
