import math

N = int(input())

X_list = []
Y_list = []

for i in range(N):
    X,Y = map(int, input().split())
    X_list.append(X)
    Y_list.append(Y)

distance_list = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        distance = math.sqrt((X_list[i]-X_list[j])**2 + (Y_list[i]-Y_list[j])**2)
        distance_list[i].append(distance)

    max_distance = max(distance_list[i])
    P = distance_list[i].index(max_distance)+1
    print(P)