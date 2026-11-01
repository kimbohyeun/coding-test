#입력받기
lenth = int(input())
weak=list(map(int,input().split()))
dist=list(map(int,input().split())) 

#취약점 거리 리스트 만들기
weak_lenth = []
for i in range(len(weak)-1):
    weak_lenth.append(weak[i+1]-weak[i])
weak_lenth.append(12+weak[0]-weak[-1]) 
print(weak_lenth)

#멀리 가는 놈부터 실행
finished_weak=[]
finished_dist=[]
for d in dist[::-1]:
    for w in weak_lenth: #취약점 거리 하나하나 뺌
        if((d-w)>=0): #그 인원이 처리 가능하다면
            d-=w
            finished_weak.append(w)
        else:
            finished_dist.append(d)
            break
    weak_lenth = [x for x in weak_lenth if x not in finished_weak] #처리한 놈은 빼기
    if(len(weak_lenth)==0): #다 처리 햇다면
        break
        
print(weak_lenth,finished_weak,len(finished_dist))

    
        
                
