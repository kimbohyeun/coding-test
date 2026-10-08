N=input()
point=[]
count=0
count_1=0
count_2=0
for i in N:
    point.append(int(i))
#123 402
for p in point:
    count+=1
    if(count<=len(point)//2):
        count_1+=p
    else:
        count_2+=p
if(count_1==count_2):
    print("LUCKY")
else:
    print("READY")

