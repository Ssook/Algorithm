# 출처 : https://www.acmicpc.net/problem/11866
n, k = map(int, input().split())
table = list(range(1, n+1))
answer = []
index = 0
while(table):
    index += k-1
    answer.append(table[index % len(table)])
    index = index % len(table)
    del table[index % len(table)]


print('<', end='')
for a in answer:
    if(a == answer[-1]):
        print(a, end='')
    else:
        print(a, end=', ')

print('>')
