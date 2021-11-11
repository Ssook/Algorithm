# 출처 : https://www.acmicpc.net/problem/1120
a, b = input().split()
answer = 0
# 두개의 길이가 같으면 단순 비교
if(len(a) == len(b)):
    for i in range(len(a)):
        if(a[i] != b[i]):
            answer += 1
    print(answer)

# 다른 경우 앞뒤로 넣어주고 비교
else:
    answers = []
    diff = len(b)-len(a)
    for i in range(diff+1):
        answer = 0
        tempA = a
        # 앞에 붙이는게 i 개, 뒤에 붙이는게 diff-i개
        for _ in range(i):
            tempA = '0'+tempA
        for _ in range(diff-i):
            tempA = tempA+'0'

        for i in range(len(tempA)):

            if(tempA[i] != b[i]):
                answer += 1
        # 새로 붙이는 거는 다 b와 같은거라고 생각
        answers.append(answer-diff)

    print(min(answers))
