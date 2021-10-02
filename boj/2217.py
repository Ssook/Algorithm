# 출처 : https://www.acmicpc.net/problem/2217
n = int(input())

weight = []
for i in range(n):
    weight.append(int(input()))

# 큰 것 부터 정렬
weight.sort(reverse=True)
answer = weight[0]
# 앞에서부터 n개까지의 리스트를 sliced에 담는다.
sliced = []
# 줄을 1,2..n개 쓰는 경우
for i in range(len(weight)):
    sliced.append(weight[i])

    
    if((weight[i])*(i+1) >= answer):
        answer = (weight[i])*(i+1)


print(answer)
