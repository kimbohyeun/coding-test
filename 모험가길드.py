N=int(input())
members=list(map(int,input().split()))
team=[]
count=0
members.sort()
for i in range(len(members)):
    team.append(members[i])
    if(max(team) <= len(team)):
        count+=1
        team.clear()
print(count)

팀을 만들고 비운다는 이 이미지를 만들어내려고 하다보니까 list로 팀을 만들고 비우는 과정을 clear()로 구현함
근데 그런식으로 안하고 숫자만 세도 충분했음 이미지에 가두는 습관을 고쳐야됨
또한 max(team)으로 비교했는데 어차피 처음에 sort를 썼으므로 항상 방금 추가된 멤버가 공포도가 최고이니
max를 굳이 쓸 필요 없었음

