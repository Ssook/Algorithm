# 출처 : https://www.acmicpc.net/problem/1085
x, y, w, h = map(int, input().split())
d = min(x, w-x, y, h-y)
print(d)
