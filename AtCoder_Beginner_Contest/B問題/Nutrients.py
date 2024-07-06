N,M = map(int, input().split())
A = list(map(int, input().split()))

X = []
for i in range(N):
    nutrients = list(map(int, input().split()))
    X.append(nutrients)

sum = 0
answer = "Yes"
for j in range(M):
    for k in range(N):
        sum = sum+X[k][j]

    if sum < A[j]:
        answer = "No"

    sum = 0
    
print(answer)