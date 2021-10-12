# 출처 : https://www.acmicpc.net/problem/9375
t = int(input())
for _ in range(t):
    n = int(input())
    dict = {}
    for i in range(n):
        name, parts = input().split()
        if(parts in dict):
            dict[parts].append(name)
        else:
            dict[parts] = [name]
    sum = 1
    for key in dict:
        sum *= (len(dict[key])+1)
    sum -= 1
    print(sum)
