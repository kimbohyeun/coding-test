k=int(input())
food_times=list(map(int,input().split()))
sorted_food_times=sorted(food_times)
count=0
zero_count=0
result_zero=0
for i in sorted_food_times:
    i-=count
    if (k-(i*(len(food_times)-zero_count))) >= 0:
        k-=(i*(len(food_times)-zero_count)) #바퀴 다 돌고 몇칸 더 갈수있냐
        count+=i #몇바퀴 돌았냐
        zero_count+=1 # 0 1 2
    elif(k//(len(food_times)-zero_count)>=1):
        count+=k//(len(food_times)-zero_count)
        k=k%(len(food_times)-zero_count)         #하나의 원소를 완전히 비우지 못하는경우 그렇지만 돌긴 하는 경우
    else:
        break

# k=2
#count=3
# 3 1 2
if(k==0):
    print(1)
else:
    for j in range(len(food_times)):
        if(food_times[j]<count and j<k):
            result_zero+=1
            k+=1
    print(k+result_zero+1)

        
    다음에 다시 풀어보기..    
