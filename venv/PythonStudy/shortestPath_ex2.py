# 문제2. 미래도시
# 플루이드 워셜 알고리즘(최단거리)

INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0 으로 초기화
for a in range(1,n+1):
    for b in range(1, n+1):
        if a == b:
             graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노트 X와 최종 목적지 노드 K를 입력받기
x,k = map(int, input().split())

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distacne = graph[1][k] + graph[k][x]

if distacne >= INF:
    print("-1")
else:
    print(distacne)