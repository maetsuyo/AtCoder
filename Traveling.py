count = 0
answer = "NO"
bool = False
t = []
x = []
y = []
coord = [0,0]

N = int(input())
for i in range(N):
    temp_t,temp_x,temp_y = map(int, input().split())
    t.append(temp_t)
    x.append(temp_x)
    y.append(temp_y)

for j in range(N):
    for k in range(0, x[j]):
        coord[0] += 1
        count += 1
        if t[0] < count:
            bool = True
            break
    if bool == True:
        exit
    for l in range(0, y[j]):
        coord += [1]
        count += 1
        if t[0] < count:
            bool = True
            break
    if bool == True:
        exit