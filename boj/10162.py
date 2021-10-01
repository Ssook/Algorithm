# 출처 : https://www.acmicpc.net/problem/10162
t = int(input())
a = 300
b = 60
c = 10

dict = {
    'a': 0,
    'b': 0,
    'c': 0,
}
if(t % 10 != 0):
    print(-1)
else:
    dict['a'] = t//a
    t -= a*dict['a']
    dict['b'] = t//b
    t -= b*dict['b']
    dict['c'] = t//c
    t -= c*dict['c']
    print(dict['a'], dict['b'], dict['c'])
