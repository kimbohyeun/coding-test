문제:큰 수의 법칙, 같은수를 몇번 연속해서 더할수있는지,배열이 무엇인지 입력받고 그 수를 총 몇번 더할지도 입력받을때 최대값이 몇인가
유형분석:최대,반례없이 지금당장의 선택이 중요
풀이: 정해진꼴이 반복되는것을 확인, 그냥 이걸 수식으로 나타내는것이 가장 빠르다고 생각\
n,m,k = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
count=m//(k+1)*(data[-1]*k+data[-2])+m%(k+1)*data[-1]
print(count)
