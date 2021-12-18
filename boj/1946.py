# 출처 : https://www.acmicpc.net/problem/1946
t = int(input())
for _ in range(t):
    n = int(input())
    answer = 0
    b = 100001

    scores = [list(map(int, input().split())) for i in range(n)]
    # 첫번째 면접 결과 순위로 정렬
    scores.sort(key=lambda x: (x[0]))

    for i in range(n):
        # 첫번째 순위로 정렬해놨으므로 두번째 면접의 결과만 비교해주면 됨
        if(scores[i][1] < b):
            b = scores[i][1]
            answer += 1

    print(answer)
