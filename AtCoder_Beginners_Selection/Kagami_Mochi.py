n = int(input())
list = []

for i in range (1, n+1):
    d = input()
    list.append(d)

print(len(set(list)))