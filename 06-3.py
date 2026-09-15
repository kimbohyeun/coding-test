''' [문제/난이도]:성적이 낮은 순서로 학생 출력하기/1

유형: 풀이 날짜: 2026-09-15 핵심 발상 (Key Idea):sorted(array,key=)

풀이 과정 및 접근법:입력을 쌍으로 입력받으니 딕셔너리 또는 튜플형식으로 입력받으면 좋겠구나, 하지만 출력이 쌍을 원하는게 아닌
                 어떤 대응하는 하나만을 요구하므로 간단하게 튜플로해도 되겠다 이후 정렬이니 sort나 sorted나 계수정렬인데
                 계수정렬을 쓸 이유가 없고 튜플이므로 sorted(array,key=)꼴을 쓰자

배운 점 및 느낀 점 (TIL):어떤 쌍에서 숫자만을 비교할때는 sorted의key기능을 이용하자
                       튜플을 입력받을때 tuple(input().split)))이것도 되지만 
                       array.append((input(),input())이런식도 된다


새로 알게 된 점: 실수했던 부분/반례: 코드 (Code) '''
def sor(array):
  return array[1]

n=int(input())
data=[]
for _ in range(n):
  data.append(tuple(input().split()))
result=sorted(data,key=sor)
for i in range(n):
  print(result[i][0],end=' ')
