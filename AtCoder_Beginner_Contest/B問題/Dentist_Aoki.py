N,Q = map(int, input().split())
T = list(map(int, input().split()))

new_T = list(set(T))
for i in new_T:
    count = T.count(i)
    if count%2 == 1:
        N -= 1

print(N)