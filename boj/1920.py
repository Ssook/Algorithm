# 출처 : https://www.acmicpc.net/problem/1920
n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
m = int(input())
targets = list(map(int, input().split()))

# 각 수마다 이분 탐색
for target in targets:
    left = 0
    right = n-1
    flag = True
    while(left <= right):
        mid = (left+right)//2
        if(numbers[mid] > target):
            right = mid-1
        elif(numbers[mid] < target):
            left = mid+1
        else:
            print(1)
            flag = False
            break
    if(flag):
        print(0)
