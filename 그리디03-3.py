문제:숫자카드게임
유형분석:정렬,최대, 영향안줌
풀이:엔터를 기준으로 행 열이 구분되니 그걸 기준으로 2차원 배열로 행 열 구분,그 배열 안에서 최소값들로 배열을 새로만들고 최대값출력
n,m=list(map(int,input().split()))
array=[]
min_num= [0]*n
for _ in range(n):
    array.append(list(map(int,input().split())))
for i in range(n):
        min_num[i]=min(array[i])
print(max(min_num))

    
    
    
    
