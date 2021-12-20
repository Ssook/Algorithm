# 출처 : https://www.acmicpc.net/problem/1013
import re
t = int(input())
for _ in range(t):
    n = input()
    p = re.compile('(100+1+|01)+')
    answer = p.fullmatch(n)

    if(answer):
        print('YES')
    else:
        print('NO')
