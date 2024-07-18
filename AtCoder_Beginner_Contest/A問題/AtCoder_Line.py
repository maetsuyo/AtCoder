N,X,Y,Z = map(int, input().split())

answer = "No"
if X > Y:
    temp = Y
    Y = X
    X = temp

if Z >= X and Z <=Y:
    answer ="Yes"

print(answer)