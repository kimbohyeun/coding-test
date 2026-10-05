첫 풀이 시도

num=int(input())
food_warehouse=list(map(int,input().split()))
strategy=[0]*2
strategy[0]=(food_warehouse[0]+food_warehouse[2])
strategy[1]=(food_warehouse[1])
count=1

for i in food_warehouse[3:]:
    count+=1
    if(count%2==0):
         if(strategy[1]+i > strategy[0]): # 1>0 0>1 반복
             choosen_number=1
         else:
             choosen_number=0
         strategy[1]+=i
    if(count%2==1):
         if(strategy[0]+i > strategy[1]): # 1>0 0>1 반복
             choosen_number=0
         else:
             choosen_number=1
         strategy[0]+=i
print(strategy[choosen_number])

홀수배열만 가져가거나 짝수배열만 가져가거나를 선택하게하는 조건임 단 10 1 1 10처럼 그런 경우가 아닌경우가 존재해서 틀림
