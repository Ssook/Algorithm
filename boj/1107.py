# 출처 : https://www.acmicpc.net/problem/1107
channel = int(input())
cur = 100
m = int(input())
answer = abs(cur-channel)
if(m == 0):
    broken = []
else:
    broken = list(map(int, input().split()))


# n번 채널로 숫자 버튼을 눌러서 이동할 수 있는지 체크
def possible(n):
    if(n == 0):
        return int(0 not in broken)
    else:
        n = str(n)
        n = list(n)
        for no in n:
            if(int(no) in broken):
                return 0
        # 갈 수 있으면 눌러야하는 버튼 갯수
        return len(n)


# i번으로 숫자버튼으로 갔다고 치고 +,- 버튼눌러서 가는 거 추가해서 계산
for i in range(1000000):
    moveChannel = i
    a = possible(moveChannel)
    if(a > 0):
        answer = min(answer, a+abs(channel-moveChannel))
print(answer)
