# 출처 : https://www.acmicpc.net/problem/2156
n = int(input())
numbers = [int(input()) for _ in range(n)]

if(n == 1):
    print(numbers[0])
    exit(0)
elif(n == 2):
    print(numbers[0]+numbers[1])
    exit(0)

d = [numbers[0], numbers[0]+numbers[1],
     max(numbers[0]+numbers[2], numbers[0]+numbers[1], numbers[1]+numbers[2])]

# dp, 현재꺼먹고 두번전꺼까지, 전꺼까지먹고 이번턴 안먹기, 현재꺼,전꺼마시고 3번전꺼
for i in range(3, n):
    d.append(max(numbers[i]+d[i-2], d[i-1], d[i-3]+numbers[i-1]+numbers[i]))

print(max(d))
