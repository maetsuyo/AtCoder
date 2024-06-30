N = int(input())

names = []
for i in range(N):
    S = input()
    names.append(S)

count = 0
for j in names:
    if j == "Takahashi":
        count += 1

print(count)