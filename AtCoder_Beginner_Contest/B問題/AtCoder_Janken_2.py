N = int(input())

users = []
T = 0
for i in range(N):
    S,C = input().split()
    users.append(S)
    T = T+int(C)

users.sort()
remain = T%N
print(users[remain])