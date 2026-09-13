''' [문제/난이도]: 시각/하

유형: 구현
풀이 날짜: 2026-09-12 
핵심 발상 (Key Idea):continue

풀이 과정 및 접근법:초에서 3이 들어가는 경우와 분에서 3이 들어가는 겨웅 시에서 3이 들어가는 경우를 각각 더하고 
                 겹치는 경우를 continue를 이용해서 제거

배운 점 및 느낀 점 (TIL):continue의 사용, 숫자의 문자열화

새로 알게 된 점: 실수했던 부분/반례: 몇시몇분몇초 이런 단위에 갇히지 말고 새롭게 생각해볼 필요가있음
코드 (Code) 
'''
t=int(input())+1
count = 0;

for h in range(t):
    if("3" in str(h)):
        count +=3600
        continue
    for m in range(60):
        if("3" in str(m)):
            count +=60
            continue
        for s in range(60):
           if("3" in str(s)):
               count +=1
print(count)
