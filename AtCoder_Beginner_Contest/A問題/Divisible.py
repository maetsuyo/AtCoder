N,K = map(int, input().split())
A = list(map(int, input().split()))

for i in A:
    if i%K == 0:
        print(int(i/K), end=" ")