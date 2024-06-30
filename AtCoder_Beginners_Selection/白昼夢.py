S = input()
words = ["eraser", "erase", "dreamer", "dream"]

for i in words:
    S = S.replace(i, "")

if S == "":
    print("YES")
else:
    print("NO")