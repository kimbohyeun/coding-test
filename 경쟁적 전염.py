from collections import deque

N,K=map(int,input().split())
examiner=[]
count=0
for i in range(N):
    examiner.append(list(map(int,input().split())))
result_s,result_y,result_x=map(int,input().split())
queue=deque() # 번호, y, x, 시간

for i in range(K): 
    for y in range(N):
         for x in range(N):
             if(examiner[y][x]==i+1):
                queue.append((i+1,y,x,count))
dx= [0,0,-1,1]
dy= [-1,1,0,0]
while(queue): # q=[1,2,3.1.1.2.3.]
    q=queue.popleft()
    if(q[3]==result_s):
        break
    for i in range(4):
        nx= q[2]+dx[i]
        ny= q[1]+dy[i]
        if (nx < 0) or (ny < 0) or (nx >= N) or (ny >= N):
            continue
        if(examiner[ny][nx]==0):
            queue.append((q[0],ny,nx,q[3]+1))
            examiner[ny][nx]=q[0]

print(examiner[result_y-1][result_x-1])



