# 출처 : https://programmers.co.kr/learn/courses/30/lessons/17678

def solution(n, t, m, timetable):
    answer = ''
    busList = [540]
    for i in range(n-1):
        busList.append(busList[-1]+t)

    timeList = []
    for time in timetable:
        timeList.append(int(time.split(':')[0])*60+int(time.split(':')[1]))
    timeList.sort()
    riders = []

    # 버스마다 사람들 태워서 riderList에 넣음, riderList는 이차원 배열로, 안의 배열은 한 버스가 태운 탑승객들의 시간
    for busArriveTime in busList:
        count = 0
        riderList = []
        # 버스 시간 내에 왔을 경우 반복
        while(timeList and timeList[0] <= busArriveTime):
            count += 1
            riderList.append(timeList.pop(0))
            # 버스 만석시 이번 버스 브레이크
            if(count == m):
                break
        riders.append(riderList)

    for i in range(len(riders)-1, -1, -1):
        # 버스가 만석이 아닌 경우 마지막 버스 도착시간에만 오면 됨
        if(len(riders[i]) < m):
            answer = busList[i]
            break
        # 버스가 만석이였던 경우 마지막으로 탑승한 승객보다 1분 먼저 와야 됨
        else:
            answer = riders[i][-1]-1
            break
    minute = (answer % 60)
    hour = (int(answer/60))
    if(minute < 10):
        minute = '0'+str(minute)
    else:
        minute = str(minute)
    if(hour < 10):
        hour = '0'+str(hour)
    else:
        hour = str(hour)
    answer = (hour + ':'+minute)

    return answer


# solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]	)
# solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]	)
