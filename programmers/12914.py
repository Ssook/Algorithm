# 출처 : https://programmers.co.kr/learn/courses/30/lessons/12914
def solution(n):
    d = [0, 1, 2]
    for i in range(3, n+1):
        d.append(d[i-1]+d[i-2] % 1234567)

    return d[n] % 1234567
