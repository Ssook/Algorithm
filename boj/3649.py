# 출처 : https://www.acmicpc.net/problem/3649
while(True):
    try:
        a = b = 0
        x = int(input()) * 10000000
        n = int(input())
        legos = []
        minDiff = 0
        for i in range(n):
            legos.append(int(input()))

        legos.sort()
        answer = -1
        # 각 원소마다 이분탐색 진행해서 더해서 x가 되는 값이 있는지 확인
        for i in range(n):
            nowLego = legos[i]
            # 짝이 되는 값
            target = x-nowLego
            l = 0
            r = n-1
            while(r >= l):
                mid = (r+l)//2
                if(legos[mid] < target):
                    l = mid+1
                elif(legos[mid] > target):
                    r = mid-1
                else:
                    # 같은 수 두번 제외하고, 차이가 더 클때만 갱신
                    if(mid != i and abs(legos[mid]-nowLego) >= minDiff):
                        answer = [legos[mid], nowLego]
                        minDiff = abs(legos[mid]-nowLego)
                    break
        if(answer == -1):
            print('danger')
        else:
            answer.sort()
            print('yes', end=' ')
            for a in answer:
                print(a, end=' ')
    except:
        break
