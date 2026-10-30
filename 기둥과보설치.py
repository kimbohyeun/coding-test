def solution(n, build_frame):
    build_num=len(build_frame)
    map=[[2]*n for _ in range(n)]
   
    for i in range(build_num):
        if(build_frame[i][3]==1): #설치일떄 
            if(build_frame[i][2]==0):#기둥이라면
               if(build_frame[i][1]==0 or map[build_frame[i][0]-1][build_frame[i][1]]==1 or map[build_frame[i][0]][build_frame[i][1]-1]==0)
                map[build_frame[i][0]][build_frame[i][1]]=0        
            else: #보라면
                if(map[build_frame[i][0]-1][build_frame[i][1]]==1 or map[build_frame[i][0]][build_frame[i][1]-1]==0):
                    map[build_frame[i][0]][build_frame[i][1]]=1
        else: #삭제일떄
            if(build_frame[i][2]==0):#기둥이라면
                if(map[build_frame[i][0]][build_frame[i][1]+1]==2 and map[build_frame[i][0]][build_frame[i][1]-1]==2 andmap[build_frame[i][0]-1][build_frame[i][1]]==2):
                    map[build_frame[i][0]][build_frame[i][1]]=2
            else: #보라면
                if(map[build_frame[i][0]+1][build_frame[i][1]]==2):
                    map[build_frame[i][0]][build_frame[i][1]]=2
                 
            #기둥이냐 보냐를 구분 이후에 기둥과 보 설치 조건에 맞게 조건 검사 후 설치 #0:기둥 1:보
    
    answer = [[]]
    return answer 



n = 5
build_frame = [
    [1, 0, 0, 1], # (1, 0) 위치에 기둥(0)을 설치(1)
    [1, 1, 1, 1], # (1, 1) 위치에 보(1)를 설치(1)
    [2, 1, 0, 1], # (2, 1) 위치에 기둥(0)을 설치(1)
    [2, 2, 1, 1], # (2, 2) 위치에 보(1)를 설치(1)
    [5, 0, 0, 1], # (5, 0) 위치에 기둥(0)을 설치(1)
    [4, 2, 1, 1], # (4, 2) 위치에 보(1)를 설치(1)
    [3, 2, 1, 1]  # (3, 2) 위치에 보(1)를 설치(1)
]

print(solution(n, build_frame))
