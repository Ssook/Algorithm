# 출처 : https://www.acmicpc.net/problem/1439
s = list(input())
# 반복해서 나온 거를 압축한 minStr
minStr = s[0]
word = s[0]
# 반복문을 돌면서 연속으로 같은 문자가 나온 문자열을 압축한다.
for i in range(1, len(s)):
    if(word != s[i]):
        minStr += s[i]
    word = s[i]

minStr = list(minStr)

# 0이나 1중 더 적은거를 뒤집는다.
print(min(minStr.count('0'), minStr.count('1')))
