# 출처 : https://www.acmicpc.net/problem/10816
n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))
numbers.sort()
answer = []


def lowerBound(target):
    lowerIndex = -1
    l = 0
    r = n-1
    while(r >= l):
        mid = (r+l)//2
        if(numbers[mid] > target):
            r = mid-1
        elif(numbers[mid] < target):
            l = mid+1
        else:
            lowerIndex = mid
            r = mid-1
    return lowerIndex


def upperBound(target):
    upperIndex = -1
    l = 0
    r = n-1
    while(r >= l):
        mid = (r+l)//2
        if(numbers[mid] > target):
            r = mid-1
        elif(numbers[mid] < target):
            l = mid+1
        else:
            upperIndex = mid
            l = mid+1

    return upperIndex


for target in targets:

    lower = lowerBound(target)
    upper = upperBound(target)
    # answer.append(upper-lower+1)
    # print(lower, upper)
    if(lower == -1):
        answer.append(0)
    else:
        answer.append(upper-lower+1)


for a in answer:
    print(a, end=' ')
