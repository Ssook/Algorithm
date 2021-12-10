# 출처 : https://www.acmicpc.net/problem/15661
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = []

# 팀이 두개로 나누어져있을 때 능력치 합산해서 차이 구하는 함수


def calc(teamA, teamB):
    scoreA = 0
    scoreB = 0

    for i in range(len(teamA)):
        for j in range(len(teamA)):
            scoreA += graph[teamA[i]-1][teamA[j]-1]

    for i in range(len(teamB)):
        for j in range(len(teamB)):
            scoreB += graph[teamB[i]-1][teamB[j]-1]

    answer.append(abs(scoreB-scoreA))


# 팀을 만들어 주기 위한 재귀 함수
def recur(index, teamA, teamB):
    if(index == n+1 and len(teamA)+len(teamB) == n):
        calc(teamA, teamB)
        return

    # 백트래킹
    teamA.append(index)
    recur(index+1, teamA, teamB)
    teamA.remove(index)
    teamB.append(index)
    recur(index+1, teamA, teamB)
    teamB.remove(index)


recur(1, [], [])

print(min(answer))
