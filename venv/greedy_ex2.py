# 문제. 모험가 길드

n = int(input())

s = list(map(int, input().split()))

# 오름차순 정렬 이후 공포도가 가장 낮은 모험가부터 확인 필요
s.sort()
result = 0
count = 0
for i in range(len(s)):
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)