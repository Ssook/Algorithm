# https://www.acmicpc.net/problem/1759
global l, c
l, c = map(int, input().split())
st = input().split()
st.sort()
global answer
answer = []


# 재귀함수
def solution(startIndex, string):
    if(len(string) > l):
        return
    if(len(string) == l and ((string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u')) >= 1 and (string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u')) <= l-2)):
        if(string not in answer):
            answer.append(string)
            return
    # 현재 문자 뒤부터 이어붙인다.
    possible = st[startIndex:]
    for p in range(len(possible)):
        solution(startIndex+1+p, string+possible[p])


string = ''
for i in range(c-l+1):
    string = st[i]
    solution(i+1, string)


for a in answer:
    print(a)
