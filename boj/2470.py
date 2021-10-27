# 출처 : https://www.acmicpc.net/problem/2470
n = int(input())
numbers = sorted(list(map(int, input().split())))
answer = []
minNo = 21000000009

# 배열안의 각 숫자마다 반복문 실행해서 이분탐색으로 다른 원소들을 더해서 비교
for i in range(len(numbers)):
    r = n-1
    l = 0
    while(r >= l):
        mid = (r+l)//2
        if (abs(numbers[mid]+numbers[i]) < abs(minNo)):
            if(i != mid):
                minNo = abs(numbers[mid]+numbers[i])
                answer = [numbers[mid], numbers[i]]
                if(numbers[mid]+numbers[i]) == 0:
                    break
        if(numbers[mid]+numbers[i]) >= 0:
            r = mid-1
        else:
            l = mid+1

answer.sort()
for a in answer:
    print(a, end=' ')
