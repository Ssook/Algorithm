# 출처 : https://www.acmicpc.net/problem/1629
a, b, c = map(int, input().split())

# 분할 정복으로 풀이
# (a*b)%c = (a%c * b%c) %c


def recur(x, y):
    if(y == 1):
        return x % c

    temp = recur(x, y//2)
    if(y % 2) == 1:
        return (x*temp*temp) % c
    else:
        return (temp*temp) % c


print(recur(a, b) % c)
