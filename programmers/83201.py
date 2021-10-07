# 출처 : https://programmers.co.kr/learn/courses/30/lessons/83201

# 성적 구하는 함수
def grade(score):
    score = int(score)
    if(score >= 90):
        return 'A'
    elif(score >= 80):
        return 'B'
    elif(score >= 70):
        return 'C'
    elif(score >= 50):
        return 'D'
    else:
        return 'F'


def solution(scores):
    answer = ''
    # 배열의 행렬을 바꾸어 새로운 배열 생성
    newScores = []
    for i in range(len(scores)):
        stdScore = []
        for j in range(len(scores[i])):
            stdScore.append(scores[j][i])
        newScores.append(stdScore)

    # newScores의 한 행은 n번 학생이 받은 점수들이다.
    for i in range(len(newScores)):
        maxScore = 0
        minScore = 0
        # 만약 최고 점수가 본인이 준 점수이고, 해당 점수가 리스트에 1개만 있다면 제외
        if(max(newScores[i]) == newScores[i][i] and newScores[i].count(newScores[i][i]) == 1):
            maxScore = newScores[i][i]
        # 최저의 경우
        if(min(newScores[i]) == newScores[i][i] and newScores[i].count(newScores[i][i]) == 1):
            minScore = newScores[i][i]

        # 만약 두 값중 하나가 0이 아니라면 본인 점수를 제외하고 평균을 구해야한다.
        if(maxScore != 0 or minScore != 0):
            answer += grade(((sum(newScores[i]) -
                            maxScore-minScore)/(len(newScores)-1)))
        else:
            answer += grade(((sum(newScores[i]) -
                            maxScore-minScore)/(len(newScores))))

    return answer
