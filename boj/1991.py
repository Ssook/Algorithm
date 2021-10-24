# 출처 : https://www.acmicpc.net/problem/1991
n = int(input())
graph = {}
preList = []
midList = []
postList = []

for i in range(n):
    p, l, r = input().split()
    graph[p] = {'left': l, "right": r}


def preOrder(node, check):
    if(node == '.'):
        return
    check[ord(node)-65] = 1
    preList.append(node)
    preOrder(graph[node]['left'], check)
    preOrder(graph[node]['right'], check)


def middleOrder(node, check):
    if(node == '.'):
        return
    check[ord(node)-65] = 1
    middleOrder(graph[node]['left'], check)
    midList.append(node)
    middleOrder(graph[node]['right'], check)


def postOrder(node, check):
    if(node == '.'):
        return
    check[ord(node)-65] = 1
    postOrder(graph[node]['left'], check)
    postOrder(graph[node]['right'], check)
    postList.append(node)


check = [0 for i in range(n)]
preOrder('A', check)
check = [0 for i in range(n)]
middleOrder('A', check)
check = [0 for i in range(n)]
postOrder('A', check)
print(''.join(preList))
print(''.join(midList))
print(''.join(postList))
