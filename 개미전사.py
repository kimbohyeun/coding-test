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

풀이:최선의 선택지를 가져가다가 지금의 최선의 선택지와 이전의 최선의 선택지를 비교한 이후에 선택, 만약 지금의 최선의 선택지를 선택했다면
그 이전이전의 최선의 선택지를 가져오도록 만듦, 각각의 최선의 수를 리스트에 저장해서 다이나믹 형식으로 만듦
num=int(input())
food_warehouse=list(map(int,input().split()))
strategy=[0]*num
strategy[0]=food_warehouse[0]
count=0
if(food_warehouse[0]>=food_warehouse[1]):
    strategy[1]=strategy[0]
    count=0
else:
    strategy[1]=food_warehouse[1]
    count=1
for i in range(2,num):           
    if(count==(i-1)): #연속해서 2개일떄 #i=2부터시작
        if(strategy[count]<strategy[count-1]+food_warehouse[i]):
            strategy[i]=strategy[count-1]+food_warehouse[i]
            count=i
        else: #채택되지않음
            strategy[i]=strategy[count]
    else: #연속하지 않아서 무조건 하는게 이득인상황
        strategy[i]=strategy[count]+food_warehouse[i]
        count=i

print(strategy[count])

정답풀이:
num = int(input())
food_warehouse = list(map(int, input().split()))

# DP 테이블(기록용) 생성
strategy = [0] * num

# 베이스 케이스 설정
strategy[0] = food_warehouse[0]
strategy[1] = max(food_warehouse[0], food_warehouse[1])

# i번째 창고를 털지 말지 결정 (count 변수 불필요)
for i in range(2, num):
    # strategy[i - 1] : 현재 창고를 안 터는 경우 (이전 최선 유지)
    # strategy[i - 2] + food_warehouse[i] : 현재 창고를 터는 경우 (이전이전 최선 + 현재 식량)
    strategy[i] = max(strategy[i - 1], strategy[i - 2] + food_warehouse[i])

# 모든 창고를 고려했을 때의 최종 최댓값 출력
print(strategy[num - 1])
max,min..  이것을 더 제대로 활용해야할듯
