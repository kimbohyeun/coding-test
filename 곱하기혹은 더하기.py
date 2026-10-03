풀이: 무조건 앞에서부터 계산해나가므로 ()))))))) 이런식의 풀이가 되는데 이는 앞의 괄호가 최대의 값을 지니게 된다면이후의 값도 최대가
되는, 앞의 선택을 최선으로 하게된다면 이후의 결과도 최선이 되는 전형적인 그리드 문제 따라서 앞의 계산을 더 큰값으로 선택하기를 반복

num=input()
array=[]
for i in num:
    array.append(int(i))
count=array[0]
for n in array[1:]:
    if(count+n > count*n):
       count+= n
    else:
        count*=n

print(count)

개선사항: max함수를 이용하면 좀 더 쉽게코드를 짤 수 있었음
