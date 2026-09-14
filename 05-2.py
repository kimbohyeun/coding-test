''' [문제/난이도]:

유형: 풀이 날짜: 2026-09-14 핵심 발상 (Key Idea):bfs

풀이 과정 및 접근법: 4방향을 탐색하는것,bfs를 떠올리는것

배운 점 및 느낀 점 (TIL):x와 y에 대한 이동이 저렇게 정형화되어있고 벗어난 경우를 무시하는것도 정형화되어있음
                      아직 확실한 감이 오지 않았지만 가까운것부터 순차적으로 살펴가는경우의 bfs를 떠올려보자

새로 알게 된 점: 실수했던 부분/반례: 코드 (Code) '''
from collections import deque

def bfs(x, y):
    # 이동할 4가지 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # Queue 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                
            # 벽인 경우(이동할 수 없는 칸) 무시
            if graph[nx][ny] == 0:
                continue
                
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    # 가장 오른쪽 아래(출구)까지의 최단 거리 반환
    return graph[n - 1][m - 1]

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# BFS를 수행한 결과 출력 (시작 위치: (0, 0))
print(bfs(0, 0))
