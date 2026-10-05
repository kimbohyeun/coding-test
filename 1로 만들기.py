풀이: 어떤 숫자든 1을 빼는 경우는 모두가 가능함, 그러므로 1을 빼는 경우와 그러지 않은 경우를 비교해서 최소가 되는 값을 구하는것
input_num = int(input())
# array[i]는 숫자 i를 1로 만드는 최소 연산 횟수를 저장
array = [0] * (input_num + 1)

for i in range(2, input_num + 1):
    # 1. 먼저 이전 숫자(i-1)에서 1을 더해오는 경우를 기본값으로 설정
    array[i] = array[i - 1] + 1
    
    # 2. 2로 나누어떨어지는 경우, 2로 나눈 위치의 횟수+1과 비교하여 더 작은 값 선택
    if i % 2 == 0:
        array[i] = min(array[i], array[i // 2] + 1)
        
    # 3. 3으로 나누어떨어지는 경우
    if i % 3 == 0:
        array[i] = min(array[i], array[i // 3] + 1)
        
    # 4. 5로 나누어떨어지는 경우
    if i % 5 == 0:
        array[i] = min(array[i], array[i // 5] + 1)

for i in range(1, input_num + 1):
    print(i, array[i])

다이나믹 프로그래밍을 알게된 좋은 문제임 
