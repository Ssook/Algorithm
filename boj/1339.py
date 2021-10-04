# 출처 : https://www.acmicpc.net/problem/1339
# 이렇게 풀면 ABB, BB, BB .. 에서 반례 생김
# n = int(input())
# words = []
# for i in range(n):
#     words.append(input())
# maxLengthWord = ''
# answer = []
# words.sort(key=lambda x: (len(x)))
# words.reverse()
# maxNo = 9
# maxLen = 0
# wordDict = {}
# for i in range(len(words)):
#     words[i] = list(words[i])
#     maxLen = max(maxLen, len(words[i]))

# for word in words:
#     for i in range(len(word), maxLen):
#         word.insert(0, '-')


# for i in range(maxLen):
#     for word in words:
#         if(word[i] != '-' and word[i] not in wordDict):
#             wordDict[word[i]] = str(maxNo)
#             maxNo -= 1

# for word in words:
#     stringNo = ''
#     for character in word:
#         if(character in wordDict):
#             stringNo = stringNo + wordDict[character]
#     answer.append(stringNo)

# answerNo = 0
# for no in answer:
#     answerNo += int(no)


#
n = int(input())
words = []
for i in range(n):
    words.append(input())
maxLengthWord = ''
answer = []
words.sort(key=lambda x: (len(x)))
words.reverse()
maxNo = 9
maxLen = 0
wordDict = {}
for i in range(len(words)):
    words[i] = list(words[i])
    maxLen = max(maxLen, len(words[i]))

# 자리수 맞추기 위해 - 넣어줌
for word in words:
    for i in range(len(word), maxLen):
        word.insert(0, '-')
    word.reverse()

# 각 자리마다 10의 제곱꼴로 가중치를 주어서 문자마다 가중치 계산
pow = 1
for i in range(maxLen):
    for word in words:
        if(word[i] in wordDict):
            wordDict[word[i]] += pow
        else:
            wordDict[word[i]] = pow
    pow *= 10

for key in wordDict:
    answer.append([key, wordDict[key]])


answer.sort(key=lambda x: (x[1]))
answer.reverse()
answerDict = {}
# 가중치가 높은 거부터 9,8,7,6... 숫자 부여
for no in answer:
    if(no[0] != '-'):
        answerDict[no[0]] = maxNo
        maxNo -= 1

# 계산과정
answer = []
for word in words:
    word.reverse()
    stringNo = ''
    for character in word:
        if(character in answerDict):
            stringNo = stringNo + str(answerDict[character])
    answer.append(stringNo)

answerNo = 0
for no in answer:
    answerNo += int(no)

print(answerNo)
