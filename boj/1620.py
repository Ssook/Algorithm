n, m = map(int, input().split())
pocketmon = {}
for i in range(n):
    key = str(i+1)
    name = input()
    pocketmon[key] = name
    pocketmon[name] = key
for _ in range(m):
    print(pocketmon[input()])
