''' [문제/난이도]:음료수얼려먹기/1.5

유형: 풀이 날짜: 2026-09-14 핵심 발상 (Key Idea):dfs를 떠올리는것

풀이 과정 및 접근법:0인 모든곳을 방문하며 1로 만들면서 세기,재귀함수

배운 점 및 느낀 점 (TIL):bfs는 모든 경로를 탐색, 모든 경우의수를 탐색 할때 사용하는것

새로 알게 된 점: 실수했던 부분/반례: 코드 (Code) '''
import sys

# N(세로), M(가로) 입력받기
N, M = map(int, sys.stdin.readline().split())

# 2차원 리스트의 맵 정보 입력받기 (붙어서 들어오는 00110 형태)
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]


# DFS 함수 정의
def dfs(x, y):
    # 1. 주어진 범위를 벗어나는 경우 즉시 종료 (격자 밖 체크)
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    # 2. 현재 노드를 아직 방문하지 않았다면 (0이라면)
    if graph[x][y] == 0:
        # 해당 노드 방문 처리 (다시 방문하지 못하도록 1로 바꿈)
        graph[x][y] = 1

        # 상, 하, 좌, 우 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)  # 상
        dfs(x + 1, y)  # 하
        dfs(x, y - 1)  # 좌
        dfs(x, y + 1)  # 우

        # 연결된 모든 0을 방문 처리 완료했으므로 True 반환
        return True

    # 이미 방문했거나(1이 된 곳) 칸막이(1)인 경우 False 반환
    return False


# 모든 위치(노드)에 대해 음료수 채우기
result = 0
for i in range(N):
    for j in range(M):
        # 현재 위치에서 DFS 수행했을 때 True가 나오면 새로운 아이스크림 발견!
        if dfs(i, j) == True:
            result += 1

# 최종 생성된 총 아이스크림 개수 출력
print(result)
