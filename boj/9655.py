# 출처 : https://www.acmicpc.net/problem/9655
n = int(input())
d = [0 for i in range(1001)]
d[1] = True
d[2] = False
d[3] = True
d[4] = False
d[5] = True
for i in range(6, n+1):
    d[i] = not d[i-3]

if d[n]:
    print('SK')
else:
    print('CY')
