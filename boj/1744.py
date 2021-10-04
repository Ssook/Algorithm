n = int(input())
minusList = []
plusList = []
answer = 0
# 양수와 음수를 분리해서 담아준다.
for i in range(n):
    a = int(input())
    if(a > 0):
        plusList.append(a)
    else:
        minusList.append(a)
minusList.sort()
plusList.sort(reverse=True)

# 양수먼저 처리
# 양수는 큰수들부터 곱해서 더하는게 가장큼
# 하지만, 1이 있을 경우 곱한 값보다 더한 값이 클수도 있으므로 처리
while(True):
    if(len(plusList) <= 1):
        break
    a = plusList.pop(0)
    b = plusList.pop(0)
    # 더한 값이 곱한 값보다 큰 경우를 분기
    if(a*b > a+b):
        answer += a*b
    else:
        answer += a+b
# 혹시 남은 수가 있다면 그냥 더하기
while(plusList):
    answer += plusList.pop(0)


# 0과 음수 처리
# 음수는 음수끼리 곱할 경우 +이고,
# 0이랑 곱하면 0이 된다. 더한 값이 곱한 값보다 클수는 없으므로 분기 필요 없음.
while(True):
    if(len(minusList) <= 1):
        break
    a = minusList.pop(0)
    b = minusList.pop(0)
    answer += a*b
while(minusList):
    answer += minusList.pop(0)

print(answer)
