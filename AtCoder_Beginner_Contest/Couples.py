N = int(input())
colors = map(int, input().split())
colors = list(colors)

count = 0
for i in range(0, N*2-2):
    if colors[i] == colors[i+2]:
        count += 1

print(count)