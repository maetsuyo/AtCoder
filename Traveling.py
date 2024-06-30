count = 0
answer = "No"
t = []
x = []
y = []
coord = [0,0]
coord[1] = coord[1]

N = int(input())
for i in range(N):
    temp_t,temp_x,temp_y = map(int, input().split())
    t.append(temp_t)
    x.append(temp_x)
    y.append(temp_y)

for j in range(N):
    if coord[0] < x[j]:
        for k in range(coord[0], x[j]):
            coord[0] += 1
            count += 1
    if coord[0] > x[j]:
        for k in range(coord[0], x[j]):
            coord[0] -= 1
            count += 1
    if t[j] < count:
        break
    if coord[1] < y[j]:
        for l in range(coord[1], y[j]):
            coord[1] += 1
            count += 1
    if coord[1] > x[j]:
        for l in range(coord[1], y[j]):
            coord[1] -= 1
            count += 1
    if t[j] < count:
        break

    if j == N-1:
        answer = "Yes"

print(answer)