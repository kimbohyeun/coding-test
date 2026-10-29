문제풀이: 이때까지 배운 다른 문제들의 종합이였고 뱀의 몸의 구현을 뱀이 다녀가는 길을 past에 남겨놓고 거기서 사과를 먹은 개수를
고려하여 가장 최근의 past만 고려하는 방식으로 코드를 짬, 코드가 길어지다 보니 오류같은것들이 많이발생함
bord_size = int(input())
num_apple = int(input())
coordinate_apple = []
for _ in range(num_apple):
    coordinate_apple.append(list(map(int, input().split())))  # [y, x] 순서로 저장

direction_num = int(input())
direction_information = []
for _ in range(direction_num):
    direction_information.append(list(input().split()))
    direction_information[-1][0] = int(direction_information[-1][0])  # 초 정보는 정수형으로

secend = 0
count = 0
direction = 0  # 0: 우, 1: 하, 2: 좌, 3: 상

body_y = 1
body_x = 1
past_body = [[body_y, body_x]]  # 뱀의 위치도 [y, x] 순서로 통일
apple_count = 0

# y, x 기준 이동 방향 벡터 (우, 하, 좌, 상)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

while True:
    # 1. 방향 전환 시간이 되었는지 확인
    if count < direction_num and secend == direction_information[count][0]:
        if direction_information[count][1] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        count += 1

    # 2. 방향에 맞춰 y, x 좌표 이동
    body_y += dy[direction]
    body_x += dx[direction]

    past_body.append([body_y, body_x])
    secend += 1

    # 3. 벽 충돌 또는 몸통 충돌 확인 ([y, x] 순서 기준)
    if ([body_y, body_x] in past_body[-(apple_count + 2):-1] or
        body_y > bord_size or body_x > bord_size or
        body_y < 1 or body_x < 1):
        break

    # 4. 사과를 먹었는지 확인 ([y, x] 순서로 비교 및 제거)
    if [body_y, body_x] in coordinate_apple:
        apple_count += 1
        coordinate_apple.remove([body_y, body_x])

print(secend,body_y,body_x)
