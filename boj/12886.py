from collections import deque
import copy

a, b, c = map(int, input().split())
# 3차원배열로 visit 관리하면 메모리초과->딕셔너리로 관리
visit = {}
queue = deque([[a, b, c]])
queue[0].sort()
answer = 0
visit[str(queue[0][0])+'-'+str(queue[0][1])+'-'+str(queue[0][2])+'-'] = 1

while(queue):
    curState = queue.popleft()
    # 현재 상태의 돌 개수가 다 같은 경우
    if(curState[0] == curState[1] and curState[1] == curState[2]):
        answer = 1
        break

    # 반복하며 비교
    for i in range(3):
        for j in range(3):
            if(i < j and curState[i] != curState[j]):
                # 돌 옮기고 새로운 상태를 정의할 newState
                newState = copy.deepcopy(curState)
                newState[j] -= newState[i]
                newState[i] += newState[i]
                newState.sort()
                # 방문 확인, 처리를 위한 과정
                key = ''
                for nV in newState:
                    key += str(nV)+'-'
                if(key not in visit):
                    visit[key] = 1
                    queue.append(newState)


print(answer)
