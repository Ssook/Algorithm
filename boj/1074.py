# 출처 : https://www.acmicpc.net/problem/1074

global r, c
n, r, c = map(int, input().split())
n = 2**n
global count
count = 0


def divide(x, y, n):
    global count
    if(n == 1):
        if(x == r and y == c):
            print(count)
        count += 1
    else:
        m = n//2
        for i in range(2):
            for j in range(2):
                # 만약 n 영역 안에 있다면 네칸에 대해서 재귀
                if(r >= x and r <= x+n and c >= y and c <= y+n):
                    divide(x+i*m, y+j*m, m)
                # 만약 n영역 안에 없다면 count를 점핑시켜야 시간초과 안남
                else:
                    count += m**2


divide(0, 0, n)
