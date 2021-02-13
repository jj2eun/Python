# 문제1. 두 배열의 원소 교체
# a 오름차순
# b 내림차순
# 하나씩 스왚
a,b = map(int, input().split())
list_a = list(map(int,input().split()))
list_b = list(map(int, input().split()))

list_a.sort()
list_b.sort(reverse=True)

for i in range(b):
    if list_a[i]<list_b[i]:
        list_a[i],list_b[i] = list_b[i],list_a[i]
    else:
        break
print(sum(list_a))