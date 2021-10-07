# 출처 : https://www.acmicpc.net/problem/10815
n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
targets = list(map(int, input().split()))
answer = []

for target in targets:
    r = len(cards)-1
    l = 0
    flag = True
    while(r >= l):
        m = (l+r)//2
        if(cards[m] < target):
            l = m+1
        elif(cards[m] > target):
            r = m-1
        else:
            answer.append('1')
            flag = False
            break
    if(flag):
        answer.append('0')

print(' '.join(answer))
