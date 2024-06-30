alice = 0
bob = 0
n = int(input())
a = input().split()
a = [int(i) for i in a]
a.sort(reverse=True)
for j in range(n):
    if j%2 == 0:
        alice += a[j]
    elif j%2 == 1:
        bob += a[j]

diff = alice-bob
print(diff)