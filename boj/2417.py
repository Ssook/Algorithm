# 출처 : https://www.acmicpc.net/problem/2417
n = int(input())

l = 0
r = n
answer = n


def check(n, q):
    if(q*q >= n):
        return True


while(r >= l):
    m = (r+l)//2
    if(check(n, m)):
        answer = min(answer, m)
        r = m-1
    else:
        l = m+1


print(answer)
