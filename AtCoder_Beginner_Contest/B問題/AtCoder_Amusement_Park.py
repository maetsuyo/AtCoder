N,K = map(int, input().split())
print(N ,K)
A = list(map(int, input().split()))

vacant_seat = K
count = 0
for i in A:
    if vacant_seat >= i:
        vacant_seat = vacant_seat-i
    elif vacant_seat < i:
        count += 1
        vacant_seat = K
        vacant_seat = vacant_seat-i

count += 1
print(count)