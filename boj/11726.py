# 출처 : https://www.acmicpc.net/problem/11726
n = int(input())
d = [0, 1, 2]
# dp
for i in range(3, n+1):
    d.append((d[i-1]+d[i-2]) % 10007)  # 여기서 모듈로 안해주면 시간초과
print(d[n] % 10007)
