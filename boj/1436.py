# 출처 : https://www.acmicpc.net/problem/1436
n = int(input())
start = '666'
l = []
# 수를 증가시키면서 666이 있으면 리스트에 추가
while(True):
    if('666' in start):
        no = int(start)
        l.append(no)
    if(len(l) == n):
        break
    no += 1
    start = str(no)

print(l[n-1])
