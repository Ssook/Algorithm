def solution(s):
    answer = []
    arr = list(s)
    arr.pop()
    arr.pop(0)
    arr.pop()
    arr.pop(0)
    splitList = ''.join(arr)

    splitList = splitList.split('},{')
    splitList.sort(key=len)
    array = []
    for str in splitList:
        temp = str.split(',')
        temp.sort()
        array.append(temp)

    answer.append(int(array[0][0]))

    for i in array:
        for j in i:
            if(int(j) not in answer):
                answer.append(int(j))

    return answer


solution("{{2,1},{2},{2,1,3},{2,1,3,4}}")
