N = int(input())
number_list = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

# 최댓값과 최솟값 초기화 (문제 조건에 맞게 아주 작은 수와 큰 수로 설정)
max_value = -1e9
min_value = 1e9

def dfs(index, current_val):
    global max_value, min_value, plus, minus, multiply, divide

    # 모든 숫자를 다 사용했다면 최댓값, 최솟값 갱신
    if index == N:
        if current_val > max_value:
            max_value = current_val
        if current_val < min_value:
            min_value = current_val
        return

    # 1. 덧셈 연산자 검사 후 호출
    if plus > 0:
        plus -= 1
        dfs(index + 1, current_val + number_list[index])
        plus += 1  # 백트래킹 원상복구

    # 2. 뺄셈 연산자 검사 후 호출
    if minus > 0:
        minus -= 1
        dfs(index + 1, current_val - number_list[index])
        minus += 1  # 백트래킹 원상복구

    # 3. 곱셈 연산자 검사 후 호출
    if multiply > 0:
        multiply -= 1
        dfs(index + 1, current_val * number_list[index])
        multiply += 1  # 백트래킹 원상복구

    # 4. 나눗셈 연산자 검사 후 호출 (파이썬의 음수 나눗셈 규칙 고려)
    if divide > 0:
        divide -= 1
        if current_val < 0:
            dfs(index + 1, -((-current_val) // number_list[index]))
        else:
            dfs(index + 1, current_val // number_list[index])
        divide += 1  # 백트래킹 원상복구

# 탐색 시작 (첫 번째 숫자를 시작 값으로, 인덱스는 1부터 시작)
dfs(1, number_list[0])

print(int(max_value))
print(int(min_value))
