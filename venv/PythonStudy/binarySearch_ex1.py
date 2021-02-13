# 문제1. 떡볶이 떡 만들기
m,n = list(map(int, input().split()))

array = list(map(int,input().split()))

start = 0
end = max(array)

result = 0

while(start <= end):
    mid = (start + end)//2
    total = 0
    for x in array:
        if x > mid:
            total += x - mid
    if total < mid:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(mid)