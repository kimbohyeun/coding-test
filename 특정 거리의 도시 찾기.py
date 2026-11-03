from collections import deque
import sys

# 빠른 입력을 위해 사용
input = sys.stdin.readline

# 1. 입력 받기
city_num, load_num, lenth_info, start_city = map(int, input().split())

# 2. 인접 리스트(Graph) 생성 - 시간 초과 방지 핵심!
graph = [[] for _ in range(city_num + 1)]
for _ in range(load_num):
    a, b = map(int, input().split())
    graph[a].append(b)  # a에서 b로 가는 도로

# 3. 최단 거리를 기록할 리스트 (-1로 초기화하여 방문 여부 겸용)
distance = [-1] * (city_num + 1)

# 출발 도시의 거리는 0으로 설정
distance[start_city] = 0

# 4. BFS 수행
queue = deque([start_city])

while queue:
    now = queue.popleft()

    # 현재 도시에서 갈 수 있는 다른 도시들 확인
    for next_city in graph[now]:
        # 아직 방문하지 않은 도시라면 (-1이라면)
        if distance[next_city] == -1:
            # 최단 거리 갱신 (이전 도시 거리 + 1)
            distance[next_city] = distance[now] + 1
            queue.append(next_city)

# 5. 거리가 lenth_info인 도시들을 찾아 출력하기
result = []
for i in range(1, city_num + 1):
    if distance[i] == lenth_info:
        result.append(i)

if result:
    result.sort()
    for city in result:
        print(city)
else:
    print(-1)
