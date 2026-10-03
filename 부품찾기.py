풀이: 이진탐색으로 요청한 부품이 데이터에 존재하는지 빠르게 찾음
N=int(input())
items=list(map(int,input().split()))
items.sort() #이진탐색을 쓰려면 데이터가 정렬되어있어야하므로
M=int(input())
requested_items=list(map(int,input().split()))

def binary_search(array,target,start,end):
    while(start<=end):
        mid=(start+end)//2
        if(array[mid]==target):
            return "yes"
        elif(array[mid]>target):
            end= mid-1    
        elif(array[mid]<target):
            start=mid+1
           
    return "no"
   
for t in requested_items:
    print(binary_search(items,t,0,len(items)-1),end=' ')
