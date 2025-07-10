a = list(map(int, input().split()))
x = int(input())
sum = 0

for i in range(len(a)):
  if i == 0:
    sum += a[i]
  else:
    sum += a[i]*(x**i)

print(sum)