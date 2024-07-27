S = input()
S = int(S.replace("ABC", ""))

answer = "No"
if 1 <= S <= 349 and S != 316:
    answer = "Yes"

print(answer)