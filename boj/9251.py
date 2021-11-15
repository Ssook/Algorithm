# 출처 : https://www.acmicpc.net/problem/9251
str1 = input()
str2 = input()
n1 = len(str1)
n2 = len(str2)

d = [[0 for i in range(n2+1)] for j in range(n1+1)]

for i in range(1, n1+1):
    for j in range(1, n2+1):
        if(str1[i-1] == str2[j-1]):
            d[i][j] = d[i-1][j-1]+1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])


print(d[-1][-1])
