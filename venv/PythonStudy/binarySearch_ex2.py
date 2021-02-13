# 문제2. 정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_left, bisect_right

def count_by_range(array, left_val, right_val):
    right_index = bisect_right(array, right_val)
    left_index = bisect_left(array, left_val)
    return right_index - left_idnex

n,x = map(int, input().split())
array = list(map(int, input().split()))
# 특정값의 첫번째위치, 마지막위치 차이 구하기

count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)