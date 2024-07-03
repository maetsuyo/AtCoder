import math

N,L,R = map(int, input().split())
num_list = []
for i in range(N):
    num_list.append(i+1)

reverse_list = []
for j in range(L, R+1):
    reverse_list.append(j)

reverse_list.reverse()
print(num_list)
print(reverse_list)