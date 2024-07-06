N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = []
for i in A:
    C.append(i)

for j in B:
    C.append(j)

C = sorted(C)

answer = "No"
bool = False
for k in range(len(C)-1):
    for l in A:
        if C[k] == l:
            for m in A:
                if C[k+1] == m:
                    answer = "Yes"
                    bool = True
                    break
            if bool:
                break
    if bool:
        break

print(answer)