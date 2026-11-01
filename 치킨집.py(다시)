size_of_map,chicken_num=map(int,input().split()) #size_of_map <= 50, chicken_num <=13
print(size_of_map,chicken_num)
city_map=[]
house_location=[]
chicken_location=[]
chicken_distance=[0]*len(chicken_location)
sum=0
n=0

for _ in range(size_of_map):
    city_map.append(list(map(int,input().split())))
for i in range(size_of_map):
    print(city_map[i])

for y in range(size_of_map):
    for x in range(size_of_map):
        if(city_map[y][x]==1):
            house_location.append((x,y))
        elif(city_map[y][x]==2):
            chicken_location.append((x,y))

for ch_x,ch_y in chicken_location:
    for hou_x,hou_y in house_location:   # 하고 절댓값으로 변환하고 치킨집 마다의 집까지의 거리의 합을 오름차순으로 정리하고 그중 chicken_num의 개수에 맞게 고르기
        chicken_distance[n]+=(abs(ch_x - hou_x) + abs(ch_y - hou_y))
    n+=1

chicken_distance.sort()
for i in range(chicken_num):
    sum+=chicken_distance[i]

print(sum)

            
            
