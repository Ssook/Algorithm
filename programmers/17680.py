# 출처 : https://programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    answer = 0
    queue = []

    if(cacheSize == 0):
        return len(cities)*5

    for city in cities:
        city = city.upper()

        if(city in queue):
            answer += 1
            queue.remove(city)
            queue.append(city)
        else:
            answer += 5
            if(len(queue) > cacheSize):
                queue.pop(0)
            queue.append(city)

    return answer


solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	)
