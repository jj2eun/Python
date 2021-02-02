# 문제. 왕실의 나이트
n = str(input())
count = 0
nx = int(n[0])
ny = 98 - int(ord(n[1]))
print(nx, ny)
matrix = [(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)]

for step in matrix:
    x = nx + step[0]
    y = ny + step[1]
    if x >= 1 and x <=8 and y >= 1 and y <= 8:
        count += 1
print(count)