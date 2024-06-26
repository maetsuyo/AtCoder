bool = False
N,Y = map(int, input().split())

for x in range(N+1):
    for y in range(N+1):
        for z in range(N+1):
            total = 10000*x + 5000*y + 1000*z
            if total > Y:
                break
            elif ((total == Y) and (N == x+y+z)):
                mx,my,mz = x,y,z
                bool = True
                break
            else:
                mx = my = mz = -1
        if bool:
            break
    if bool:
        break
print(mx, my, mz)