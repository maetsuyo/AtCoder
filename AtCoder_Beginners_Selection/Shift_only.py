count = 0
n = int(input())
a = input().split()
bool = True
while bool == True:
    for i in range(n):
        b = int(a[i])
        if b%2 == 0:
            a[i] = b/2
        if b%2 == 1:
            bool = False

    if bool == True:
        count+=1

print(count)