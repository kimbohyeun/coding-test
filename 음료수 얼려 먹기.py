문제유형: 주변에 연결된걸 줄줄이 찾아봐야하는 유형 -> 깊이우선탐색(dfs)
풀이:상하좌우를 전부 1로 채우고 주변 상하좌우를 모두 채웠다면 카운트를 1증가시켜야댐 이걸 이용한 방법이 2중 반복문을 이용해서
처음부터 끝까지 쭉 살피다가 처음으로 0을 만나면 그 0과 연결된 0들을 전부 1로 만듬- > 처음에 0을 만날때의 수를 세준다면 그것이
만들어지는 얼린 음료수의 개수가 됨 이후에 만날 0은 처음에 만났던 0과는 연결이 안된0일테니(연결됐다면 1로 바뀌니까)
N,M=map(int,input().split())
ice_cube_tray=[list(map(int,input())) for _ in range(N)]
count=0
def dfs (ice_cube_tray, x,y):
    ice_cube_tray[x][y]=1
    if(x+1 < N and ice_cube_tray[x+1][y]==0): #오른쪽
        dfs(ice_cube_tray,x+1,y)
    if(x-1 >=0 and ice_cube_tray[x-1][y]==0): #왼쪽
        dfs(ice_cube_tray,x-1,y)
    if(y+1 < M and ice_cube_tray[x][y+1]==0): #위
        dfs(ice_cube_tray,x,y+1)
    if(y-1 >= 0 and ice_cube_tray[x][y-1]==0): #아래
        dfs(ice_cube_tray,x,y-1)
for i in range(N):
    for j in range(M):
        if(ice_cube_tray[i][j]==0):
            dfs(ice_cube_tray,i,j)
            count+=1
print(count)
