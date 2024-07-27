A = list(map(int, input().split()))
B = list(map(int, input().split()))

Takahashi_sum = 0
for i in A:
    Takahashi_sum = Takahashi_sum+i

Aoki_sum = 0
for j in B:
    Aoki_sum = Aoki_sum+j

print(Takahashi_sum - Aoki_sum + 1)