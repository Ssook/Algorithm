# 출처 : https://www.acmicpc.net/problem/17626
n = int(input())
d = [0,1]

# d[i]= d[i-j*j]+1
for i in range(2,n+2):
    minNo  = 9999999999
    j = 1
    while(j*j<=i):
        index = i-j*j
        minNo = min(minNo,d[index])
        j+=1
    d.append(minNo+1)
print(d[n])