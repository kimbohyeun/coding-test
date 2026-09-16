N,K= map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.sort() #123
B.sort(reverse=True) #321

for i in range(K):
    if(A[i] >= B[i]):
        K=i
        break
        
for i in range(K):
    A[i],B[i]=B[i],A[i]

print(sum(A))
K값을 따로 찾는게 아닌 그냥 박치기해도됨
