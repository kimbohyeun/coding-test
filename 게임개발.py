문제:게임개발
풀이:첫 시도에는 동,서,남,북 각각 바라보는 방향 따라서 함수를 선언해서 풀어보려 함 ->너무 복잡 
그래서 왼쪽으로 돌아보는 함수를 만들고 이동과 후진은 따로 만들어놓아서 해결했음



n, m = map(int, input().split())  # 맵 크기 N, M
position_x, position_y, direction = map(int, input().split())  # X, Y, 방향 한 번에 입력
position = [position_x, position_y]

game_map = []
for _ in range(n):
    game_map.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
visited[position[0]][position[1]] = True  # 첫 위치 방문 처리

count = 0
move_num = 1  # 첫 위치 포함

dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# while (count != 4) 대신 while True 사용
while True:
    turn_left()
    count += 1
    
    position_x = position[0] + dx[direction]
    position_y = position[1] + dy[direction]
    
    # 이동 가능 (육지이고 방문 안 함)
    if game_map[position_x][position_y] == 0 and not visited[position_x][position_y]:
        position[0] = position_x
        position[1] = position_y
        visited[position_x][position_y] = True
        count = 0
        move_num += 1
        continue
    
    # 4방향 모두 갈 수 없는 경우 후진 시도
    if count == 4:
        move_back = (direction + 2) % 4
        back_x = position[0] + dx[move_back]
        back_y = position[1] + dy[move_back]
        
        # 뒤가 육지라면 후진
        if game_map[back_x][back_y] == 0:
            position[0] = back_x
            position[1] = back_y
            count = 0  # 4방향 확인 카운트 리셋
        # 뒤가 바다라면 게임 종료
        else:
            print(move_num)
            break
