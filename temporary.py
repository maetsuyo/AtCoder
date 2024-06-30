count = 0
answer = "No"
t = []
x = []
y = []
coord = [0,0]
coord_x = coord[0]
coord_y = coord[1]

N = int(input())
for i in range(N):
    temp_t,temp_x,temp_y = map(int, input().split())
    t.append(temp_t)
    x.append(temp_x)
    y.append(temp_y)

# t = [3, 6]
# x = [1, 1]
# y = [2, 1]

for j in range(N):
    if coord_x < x[j]:
        for k in range(coord_x, x[j]):
            coord[0] += 1
            count += 1
    if coord_x > x[j]:
        for k in range(coord_x, x[j]):
            coord[0] -= 1
            count += 1
    if t[0] < count:
        break
    if coord_y < y[j]:
        for l in range(coord_y, y[j]):
            coord[1] += 1
            count += 1
    if coord_y > x[j]:
        for l in range(coord_y, y[j]):
            coord[1] -= 1
            count += 1
    if t[j] < count:
        break

    coord_x = coord[0]
    coord_y = coord[1]

    if j == N-1:
        answer = "Yes"

print(answer)