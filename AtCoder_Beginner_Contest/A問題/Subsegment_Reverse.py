N,L,R = map(int, input().split())
num_list = []
for i in range(N):
    num_list.append(i+1)

reverse_list = []
for j in range(L, R+1):
    reverse_list.append(j)

reverse_list.reverse()

L -= 1
for k in reverse_list:
    num_list.insert(L, k)
    L += 1
    del num_list[L]

print(*num_list)