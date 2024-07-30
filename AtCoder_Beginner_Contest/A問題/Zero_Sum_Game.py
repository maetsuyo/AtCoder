N = int(input())
A = list(map(int, input().split()))

sum = 0
for i in A:
    sum = sum+i

print(sum * -1)