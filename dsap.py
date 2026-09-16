N=int(input())
item=list(map(int,input().split())) 
M=int(input())
buy=list(map(int,input().split())) 
response=[]
item.sort() 

def binary(array):
    for i in range(M):
        target=buy[i]
        start=0
        end=N-1
        while True:
            if(start > end):
                response.append('no')
                break
            mid= (start + end)//2
            if(array[mid]==target):
                response.append('yes')
                break
            elif(array[mid]>target):
                end= mid-1
            else:
                start= mid+1
binary(item)
for j in range(M):
    print(response[j],end=' ')
