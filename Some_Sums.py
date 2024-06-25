total = 0
n,a,b = map(int, input().split())
for i in range(n+1):
    if len(str(i)) == 1:
        if (i >= a) and (i <= b):
            total += i
    else:
        spilt = [int(j) for j in str(i)]
        sum = 0
        for k in spilt:
            sum += k
        if (sum >= a) and (sum <= b):
            total += i

print(total)