# 출처 : https://www.acmicpc.net/problem/17219
import sys
n, m = map(int, sys.stdin.readline().split())
dict = {}
for i in range(n):
    site, pw = sys.stdin.readline().split()
    dict[site] = pw

for j in range(m):
    aa = input()
    print(dict[aa])
