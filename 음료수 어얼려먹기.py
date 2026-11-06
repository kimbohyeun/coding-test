Height, Width = map(int, input().split())
visited = [[False]*Width for _ in range(Height)]
count = 0
Ice_Case = [list(map(int, input().strip())) for _ in range(Height)]
# 0: 아이스크림 1: 칸막이
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def Make_ice(Ice_Case, x, y, visited):         
    if visited[y][x] == False and Ice_Case[y][x] == 0:
         visited[y][x] = True
         Ice_Case[y][x] = 1
         for i in range(4):
             nx = x + dx[i]
             ny = y + dy[i]
             # 수정된 부분: 0 이상 Width/Height 미만으로 범위 체크
             if 0 <= nx < Width and 0 <= ny < Height:
                 Make_ice(Ice_Case, nx, ny, visited)

for h in range(Height):
    for w in range(Width):
        if visited[h][w] == False and Ice_Case[h][w] == 0:
            count += 1
            Make_ice(Ice_Case, w, h, visited)
            
print(count)
