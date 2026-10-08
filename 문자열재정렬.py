array=input()
result=[]
last_result=[]
count_int=0
add_int=0

for i in array:
    result.append(ord(i))
    if(ord(i)<=57):
        count_int+=1
        add_int+=int(i)
        
result.sort()

for j in range(count_int,len(array)):
    last_result.append(chr(result[j]))
last_result.append(add_int)

for m in last_result:
    print(m,end='')


더 최적화가 가능한 풀이임
또한 숫자가 없어도 0이 출력되는 예외가 존재함
isalpha같은 함수를 사용했다면 더 깔끔했음
