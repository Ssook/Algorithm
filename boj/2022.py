# 출처 : https://www.acmicpc.net/problem/2022
import math
x, y, c = map(float, input().split())

# d의 값을 임의로 설정해봄, d는 h가 c에 가장 가까워지는 수
left = 0
right = min(x, y)
# 기존처럼 while, +1 ,-1 을 사용하면 실수를 다룰 수 없다.
for i in range(10000):
    # 수학식
    mid = (left+right)/2.0
    x2 = math.pow(x, 2)
    y2 = math.pow(y, 2)
    d2 = math.pow(mid, 2)
    h1 = math.sqrt(x2-d2)
    h2 = math.sqrt(y2-d2)

    h = (h1*h2)/(h2+h1)
    if(h < c):
        right = mid
    else:
        left = mid

print(round(left, 3))
