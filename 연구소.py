from collections import deque
from itertools import combinations
import sys

# 재귀 깊이 제한을 넉넉하게 늘려줍니다 (예: 10만 또는 100만)
sys.setrecursionlimit(10**6)

def Virus_Spread(Map, virus):
    # 전달받은 바이러스 좌표들을 하나씩 확인하며 퍼뜨립니다.
    for v in virus:
        for m in range(4):
            ny = v[0] + dx[m]
            nx = v[1] + dy[m]
            
            # 1. 범위 체크: 0 이상 N 미만, 0 이상 M 미만이어야 합니다.
            # 2. 조건 체크: 이동한 곳이 빈칸(0)이어야 합니다.
            if 0 <= ny < N and 0 <= nx < M:
                if Map[ny][nx] == 0:
                    Map[ny][nx] = 2          # 바이러스 퍼뜨리기
                    virus.append((ny, nx))   # 튜플 형태로 통째로 추가!
    Virus_Spread(Map,virus)
    return Map

N,M= map(int,input().split())
Map=[]
virus=[]
wall=[]
for i in range(N):
    Map.append(list(map(int,input().split())))
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for y in range(N):
    for x in range(M):
        if(Map[y][x]==2):
            virus.append((y,x))
        elif(Map[y][x]==1):
            wall.append((y,x))

count=0
last_result=[] 
added_wall=list(combinations(empty,3)) #3개의 추가된 벽을 반영하는 모든 경우의 수 
#2: 바이러스 1: 벽 0:빈칸
for w1, w2, w3 in added_wall:
    # w1, w2, w3는 각각 (y, x) 형태의 튜플
    y1, x1 = w1
    y2, x2 = w2
    y3, x3 = w3
    NMap=Map
    # NMap에 각각 벽(1) 세우기
    NMap[y1][x1] = 1
    NMap[y2][x2] = 1
    NMap[y3][x3] = 1
    result=Virus_Spread(NMap,virus)
    for y in range(N):
        for x in range(M):
            if(result[y][x]==0):
                count+=1
    last_result.append(count)
print(min(last_result))
