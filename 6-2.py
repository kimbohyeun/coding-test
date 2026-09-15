''' [문제/난이도]:위에서아래로/1

유형: 풀이 날짜: 2026-09-15 핵심 발상 (Key Idea):sorted,reverse=True

풀이 과정 및 접근법:특별한 상황이 아니니 라이브러리함수를 사용해야겠다

배운 점 및 느낀 점 (TIL):sorted()는 원본을 훼손하지 않고 반환값이 있음 또한 리스트뿐만 아니라 다른것도 다 됨
                      .sort():는 파괴적이며 리스트에만 적용가능함

새로 알게 된 점: 실수했던 부분/반례: 코드 (Code) '''
n=int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
numbers=sorted(numbers,reverse=True)
for i in range(n):
  print(numbers[i],end=' ')
