k=int(input())
food_times=list(map(int,input().split()))
result=0
count=0
zero_count=0
for _ in range(k):                   
    if(food_times[count]==0):
        count+=1
        zero_count+=1
    else:
        food_times[count]-=1
        count+=1
    
    if(count==len(food_times)):
        count=0
if(zero_count==len(food_times)):
    result=zero_count
else: 
    if(count==len(food_times)-1):
        count=1
    else:
        count+=1
    result=count
print(result)
