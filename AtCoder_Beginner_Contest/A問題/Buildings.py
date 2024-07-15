N = int(input())
H = list(map(int, input().split()))

answer = -1
for i in range(1, N):
    if H[i] > H[0]:
        answer = i+1
        break

print(answer)