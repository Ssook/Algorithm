# 출처 : https://www.acmicpc.net/problem/16922
n = int(input())
# 사용 가능한 수
origin = [1, 5, 10, 50]

# 인덱스만큼의 로마숫자를 사용해서 만들 수 있는 다른 수의 갯수 d, ex)d[1]은 숫자 한개로 만들 수 있는 서로 다른 수들의 리스트
d = [[], [1, 5, 10, 50]]

# d[n]의 모든 원소에 origin 숫자들을 하나씩 더해서 d[n+1]을 만든다.
for i in range(1, n):
    l = []
    for no in origin:
        for exist in d[i]:
            if((exist+no) not in l):
                l.append(exist+no)
    d.append(l)

print(len(d[n]))
