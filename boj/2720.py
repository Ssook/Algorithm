# 출처 : https://www.acmicpc.net/problem/2720
t = int(input())

# 가치
a = 25
b = 10
c = 5
d = 1

# 거스름돈의 개수
c1 = 0
c2 = 0
c3 = 0
c4 = 0

for i in range(t):
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    n = int(input())
    # n = 100*n
    c1 = n//a
    n -= a*c1
    c2 = n//b
    n -= b*c2
    c3 = n//c
    n -= c * c3
    c4 = n//d

    print(c1, c2, c3, c4)
