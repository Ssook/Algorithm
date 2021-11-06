# 출처 : https://www.acmicpc.net/problem/5598
word = input()
answer = ''
for w in word:
    answer += chr(((ord(w)-68) % 26)+65)

print(answer)
