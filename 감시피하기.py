from itertools import combinations

N=int(input())
result=[]
Map=[]
T_Map=[]
S_Map=[]

X_Map=[]
for _ in range(N):
    Map.append(list(input().split()))
    
for y in range(N):
    for x in range(N):
        if(Map[y][x]=='T'):
            T_Map.append((y,x))
        elif(Map[y][x]=='S'):
            S_Map.append((y,x))
        elif(Map[y][x]=='X'):
            X_Map.append((y,x))
                        
def unsafe_zone(object):
    for ty,tx in T_Map:
        for sy,sx in S_Map:
            if(ty==sy):
                if not(any(ty == t[0] for t in object)): #걸렸다
                    return 0
            if(tx==sx):
                if not(any(tx == t[1] for t in object)):
                    return 0
    return 1
                    
for P_Map in (list(combinations(X_Map,3))):
    result.append(unsafe_zone(P_Map))

if(1 in result):
    print("YES")
else:
    print("NO")
