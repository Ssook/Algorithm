# 출처 : https://www.acmicpc.net/problem/2133
n = int(input())
d = [1, 0, 3, 0, 11]
for i in range(5, n+1):
    # 홀수인 경우 무조건 못 채움
    if(i % 2 == 1):
        d.append(0)
    else:
        count = d[i-2]*3 # 기본적으로 두번째칸 전의 경우의수에 *3 (가로3,가로1세로2,세로2,가로1)
        # 중간에 겹치는 애들 계산
        for j in range(i-4, -1, -2):
            count += d[j]*2
        d.append(count)

print(d[n])
