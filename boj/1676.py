# 출처 : https://www.acmicpc.net/problem/1676
n = int(input())

num = 1
for i in range(1, n+1):
    num *= i
count = 0
stNum = list(str(num))
while(stNum):
    p = stNum.pop()
    if(p != '0'):
        break
    elif (p == '0'):
        count += 1

print(count)
