max = 0
maxIndex = 0
for i in range(9):
    a = int(input())
    if(a > max):
        maxIndex = i
        max = a

print(max)
print(maxIndex+1)
