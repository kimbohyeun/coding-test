문제:상하좌우
유형분석:
풀이:문제에서 이동횟수와 n의 범위가 매우작음 -> 그냥 풀어도 아무문제 없음
num=int(input())
direction=input().split()
x,y=1,1
#R: +1  D: +1
for i in direction:
    if(i=='R'):
        x+=1
    if(i=='L' and x>1):
        x+=-1
    if(i=='D'):
        y+=1
    if(i=='U' and y>1):
        y+=-1
print(y,x)
