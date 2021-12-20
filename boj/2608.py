# 출처 : https://www.acmicpc.net/problem/2608
no = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# 숫자 받아서 문자열로 돌려주는 함수


def toStr(n):
    s = ''
    # 천의 자리
    m = n//1000
    for i in range(m):
        s += 'M'
        n -= 1000

    # 백의 자리
    c = n//100
    if(c == 9):
        s += 'CM'
        n -= 900
    elif(5 < c < 9):
        s += 'D'
        n -= 500
        for i in range(c-5):
            s += 'C'
            n -= 100
    elif(c == 5):
        s += 'D'
        n -= 500

    elif(c == 4):
        s += 'CD'
        n -= 400
    else:
        for i in range(c):
            s += 'C'
            n -= 100

    # 십의 자리
    x = n//10
    if(x == 9):
        s += 'XC'
        n -= 90
    elif(5 < x < 9):
        s += 'L'
        n -= 50
        for i in range(x-5):
            s += 'X'
            n -= 10
    elif(x == 5):
        s += 'L'
        n -= 50
    elif(x == 4):
        s += 'XL'
        n -= 40
    else:
        for i in range(x):
            s += 'X'
            n -= 10

    # 일의 자리
    one = n//1
    if(one == 9):
        s += 'IX'
        n -= 9
    elif(5 < one < 9):
        s += 'V'
        for i in range(one-5):
            s += 'I'
            n -= 1
    elif(one == 5):
        s += 'V'
        n -= 5
    elif(one == 4):
        s += 'IV'
        n -= 4
    else:
        for i in range(one):
            s += 'I'
            n -= 1

    return s

# 문자열을 숫자로 돌려주는 함수


def toNumber(s):
    stack = []
    total = 0
    for i in range(len(s)):
        nowNo = no[s[i]]
        if(not stack):
            stack.append(nowNo)
        # 작은 숫자가 앞에 오는 경우
        elif(stack[-1] < nowNo):
            prevNo = stack.pop()
            stack.append(nowNo-prevNo)
        else:
            stack.append(nowNo)
    return sum(stack)


a = input()
b = input()
sum = toNumber(a)+toNumber(b)
print(sum)
print(toStr(sum))
