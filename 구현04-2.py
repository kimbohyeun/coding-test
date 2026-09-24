 문제: 시각
풀이:숫자에 대한 접근과 3이라는 문자에 대한 접근 각각있음, 후자가 구현이 편해서 후자

num= int(input())
result=0

for i in range(num+1):
    for j in range(60):
        for m in range(60):
            if('3' in str(i) + str(j) + str(m)):
                result+=1
print(result)
