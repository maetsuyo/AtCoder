N,A = map(int, input().split())
T = list(map(int, input().split()))

bool = False
time = 0    
for i in range(N):
    while bool == False:
        if time >= T[i]:
            time += A
            print(time)
            bool = True
        if time < T[i]:
            time += 1
    bool = False