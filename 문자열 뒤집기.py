풀아: 그냥 직접 써보다 보니까 특정한 패턴이 반복됨 그것을 코드로 표현
num = input()
count = 0

# 인접한 두 문자가 다르면 경계 개수(count) 증가
for i in range(len(num) - 1):
    if num[i] != num[i + 1]:
        count += 1

# 문자가 바뀐 적이 없으면(모두 같은 숫자면) 0회, 바뀌었으면 (count + 1) // 2 회
if count == 0:
    print(0)
else:
    print((count + 1) // 2)
