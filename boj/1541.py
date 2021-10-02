from collections import deque
numbers = input()

# 변환된 식을 넣은 real
real = deque([])
queue = deque([])
isMinus = False
for ch in numbers:
    if(ch != '+' and ch != '-'):
        queue.append(ch)
    else:
        # -가 한번이라도 나오면 그 다음 숫자들은 모두 다 -
        if(ch == '-'):
            isMinus = True

        stringNumber = ''
        while(queue):
            stringNumber += queue.popleft()
        real.append(int(stringNumber))
        if(isMinus):
            real.append('-')
        else:
            real.append('+')

# 큐에 남아 있는 수를 넣어줌
leftStringNumber = ''
while(queue):
    leftStringNumber += queue.popleft()
real.append(int(leftStringNumber))

# real에는 변환 된 식이 들어가 있으므로 계산만 해주면 됨
total = real.popleft()
while(real):
    now = real.popleft()
    if(now == '-'):
        total -= real.popleft()
    elif(now == '+'):
        total += real.popleft()

print(total)
