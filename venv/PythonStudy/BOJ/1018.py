n, m = map(int, input().split())
data = []
mini = []
for i in range(n):
    data.append(list(input()))


for a in range(n - 7):
    for b in range(m - 7):
        count1 = 0
        count2 = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if ((i + j) % 2) != 0:
                    if data[i][j] != 'W': count1 += 1
                    if data[i][j] != 'B': count2 += 1
                else:
                    if data[i][j] != 'B': count1 += 1
                    if data[i][j] != 'W': count2 += 1
        mini.append(count1)
        mini.append(count2)

print(min(mini))