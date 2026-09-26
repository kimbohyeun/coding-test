n,m=int(input().split())
first_position=list(map(int,lnput().split()))
direction=int(input())
game_map=[]
for _ in range(n):
    game_map.append(list(map(int,input().split()))) #[[1,1,1,1]
count=0                                               [1,0,0,1]
move_num=0                                            [1,1,0,1]
                                                      [1,1,1,1]]

visited = [[False] * m for _ in range(n)]
def move_east(posi,direc):
    #동쪽을 바라보는 기준
    if(count<4):
        count+=1
    else: #4방향 모두 살펴본 경우
        if(game_map[posi[0]][posi[1]-1]==1): #뒤가 바다라면
            print(move_num) #이동횟수 출력,마무리
        elif(game_map[posi[0]][posi[1]-1]==0): # 뒤가 육지라면
            position=[posi[0]][posi[1]-1] #뒤로이동
            if(visited[posi[0]][posi[1]-1]==False): #이동한 곳이 가보지않은곳이라면
                visited[posi[0]][posi[1]-1]=True #가본곳으로하고
                move_num+=1                #이동횟수 늘리고
            move_east(position,1) #바라보는 방향유지,위치만 변경해서 다시 시작
            
    if(visited[posi[0]-1][posi[1]]==Flase and
       game_map[posi[0]-1][posi[1]]==0 ):,가보지않았고 육지라면
        visited[posi[0]-1][posi[1]]==True #
        posi=[posi[0]-1][posi[1]] #위치 옮기고
        direc=0 #시선 옮기고
        move_num+=1
        move_north(posi,0) #옮긴 시선 기준으로 다시 함수호출
        
    elif(visited[posi[0]-1][posi[1]]==True or
        game_map[posi[0]-1][posi[1]]==1): #가보거나 바다라면
        direc=0 #시선만 옮기고
        move_north(posi,direc) 함수 호출
        

    game_map[position[0]][position[1]-1] #왼쪽보기
    game_map[position[0]+1][position[1]] #아래보기
    game_map[position[0]][position[1]+1] #오른쪽보기
