# 출처 : https://programmers.co.kr/learn/courses/30/lessons/12900
def solution(n):
    d = [0, 1, 2]
    # dp
    for i in range(3, n+1):
        d.append((d[i-1]+d[i-2]) % 1000000007)  # 여기서 모듈로 안해주면 시간초과
    return d[n] % 1000000007
