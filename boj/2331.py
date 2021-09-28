# 출처 : https://www.acmicpc.net/problem/2331
a, p = input().split()
p = int(p)

check = [0 for _ in range(1000000)]
stack = [a]
count = 1
# 숫자 인덱스에 몇번째인지 카운트값 넣어주다가, 이미 카운트 값이 들어가있으면 해당 값-1
while(True):
    nowNode = stack.pop()
    if(check[int(nowNode)] > 0):
        print(check[int(nowNode)]-1)
        break
    check[int(nowNode)] = count

    sum = 0
    for n in nowNode:
        sum += int(n)**p

    stack.append(str(sum))
    count += 1
