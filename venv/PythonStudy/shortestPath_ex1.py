# 문제1. 전보
import heapq
INF = int(1e9)

def dijkstra(start):
    q = []

    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[npw]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))


n,m,start = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 우선순위 큐를 이용한 다익스트라 알고리즘

# 모든 간선 정보를 입력받기
for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))

dijkstra(start)

count = 0

max_distance = 0

for d in distance:
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)

print(count-1, max_distance)