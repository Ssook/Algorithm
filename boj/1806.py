# 출처 : https://www.acmicpc.net/problem/1806

n, target = map(int, input().split())
numbers = list(map(int, input().split()))
answer = []
# 투 포인터 이용
l = r = 0
total = numbers[0]
while(r >= l):
    if(total >= target):
        answer.append(r-l+1)
        total -= numbers[l]
        l += 1
    else:
        r += 1
        if(r == n):
            break
        total += numbers[r]

if answer:
    print(min(answer))
else:
    print(0)
