풀이:자신보다 작은 볼링공의 수는 뺴고 자신의 무게의 수x자신보다 큰 무게의 수 이 식을 2중반복문 없이 구현하는게 핵심이였음
무게별 수를 딕셔너리 구조를 이용해서 선언하고 (전체-본인의수-이전까지의 수)*본인의 수를 이용해서 값을 구함
딕셔너리 대신 리스트를 사용할수도 있었음

num,max_pound=map(int,input().split())
bolling_balls=list(map(int,input().split()))
bolling_balls.sort()
ball={}
count=0
result=0

for i in bolling_balls:
    if(not(i in ball)):
        ball[i]=1
    else:
        ball[i]+=1
        
for key in ball:
    result+=(num-ball[key]-count)*ball[key]
    print(result)
    count+=ball[key]
    
print(result)
