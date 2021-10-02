# 출처 : https://www.acmicpc.net/problem/1931
n = int(input())
timeList = []
for i in range(n):
    time = list(map(int, input().split()))
    timeList.append(time)

# 종료시간 - 시작 시간 순으로 정렬
timeList.sort(key=lambda x: (x[1], x[0]))

startTime = timeList[0][0]
endTime = timeList[0][1]
answer = 1
# 종료시간이 가장 빠른 거 부터 회의실을 배정
for i in range(1, n):
    if(timeList[i][0] >= endTime):
        startTime = timeList[i][0]
        endTime = timeList[i][1]
        answer += 1

print(answer)
