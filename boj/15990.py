# 출처 : https://www.acmicpc.net/problem/15990
t = int(input())
d = [[0 for i in range(4)] for _ in range(100001)]
d[1][1] = 1
d[1][0] = 1
d[2][2] = 1
d[2][0] = 1
d[3][1] = 1  # 2,1
d[3][2] = 1  # 1,2
d[3][3] = 1  # 3
d[3][0] = 3
d[4][1] = 2  # 3,1, 1,2,1
d[4][2] = 0
d[4][3] = 1  # 1,3
# d[4]=3  # 1,2,1  3,1  1,3
# d[i][j] i를 만들기 위해 j로 끝나는 경우의 수
# d[i][0] = i를 만들기 위한 경우의 수
for i in range(4, 100001):
    for count in range(1, 4):
        d[i][count] = (d[i-count][0]-d[i-count][count]) % 1000000009
    d[i][0] = sum(d[i][1:4]) % 1000000009


for _ in range(t):
    n = int(input())
    print(d[n][0])
