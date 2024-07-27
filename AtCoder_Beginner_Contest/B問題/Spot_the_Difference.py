N = int(input())
A = []
B = []

def Append(listName):
    for i in range(N):
        word = input()
        listName.append(list(word))

Append(A)
Append(B)

for j in range(N):
    for k in range(N):
        if A[j][k] != B[j][k]:
            print(j+1, k+1)