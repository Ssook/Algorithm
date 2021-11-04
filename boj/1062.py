# 출처 : https://www.acmicpc.net/problem/1062
from itertools import combinations

n, k = map(int, input().split())
words = [input() for i in range(n)]
answer = []
k = k-5  # antic는 무조건 가르쳐야 되니까 5개 빼주자
if(k < 0):
    print(0)
    exit(0)

available = set(['a', 'n', 'c', 't', 'i'])
characters = ['b', 'd', 'e', 'f', 'g', 'h',  'j', 'k', 'l',
              'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
for com in combinations(characters, k):
    # 모든 조합마다 체크
    count = 0
    for c in com:
        available.add(c)
    # 단어 체크
    for i in range(n):
        word = words[i]
        isAvailable = True
        for w in word:
            if(w not in available):
                isAvailable = False
                break
        if(isAvailable):
            count += 1

    answer.append(count)
    # 원상복구
    for c in com:
        available.remove(c)

print(max(answer))
