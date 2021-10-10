# 출처 : https://www.acmicpc.net/problem/1181
from collections import deque
n = int(input())
words = []
for i in range(n):
    word = input()
    if(word not in words):
        words.append(word)

words.sort(key=lambda x: (len(x)))

queue = deque(words)
# print(words)
splitWords = []
w = len(words[0])
stack = []
while(queue):
    cur = queue.popleft()
    if(len(cur) == w):
        stack.append(cur)
        w = len(cur)
    else:
        splitWords.append(stack)
        stack = []
        stack.append(cur)
        w = len(cur)

# print(stack)
if(stack):
    splitWords.append(stack)
# print(splitWords)

for i in range(len(splitWords)):
    splitWords[i].sort()

for i in range(len(splitWords)):
    for j in range(len(splitWords[i])):
        print(splitWords[i][j])
