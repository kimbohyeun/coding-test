def solution(n, build_frame):
    build_num=len(build_frame)
    for i in range(build_num):
        if(build_frame[i][2]==0):
            pass
        else:
            pass #기둥이냐 보냐를 구분 이후에 기둥과 보 설치 조건에 맞게 조건 검사 후 설치 또는 삭제
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
