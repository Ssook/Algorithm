# 출처 : https://www.acmicpc.net/problem/1789
s = int(input())
sum = 0

# 가장 많은 수는 1,2,3 .. 처럼 작은 수부터 더하고 큰거부터 부족한 만큼 채우는 경우이다.
for i in range(1, 999999):
    sum += i
    if(sum > s):
        print(i-1)
        break
