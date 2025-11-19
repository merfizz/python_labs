s = str(input("in:"))
i = 1
flag1 = 0
flag2 = 0
flag3 = 0
ind2 = 0
rang = 0

out = ""
for i in range(len(s)):
    if (flag1 == 0) and (ord(s[i]) >= 65) and (ord(s[i]) <= 90):
        out = out + s[i]
        ind1 = i
        flag1 = 1
    if (flag1 == 1) and ((ord(s[i]) >= 48) and (ord(s[i]) <= 57)) and (flag2 == 0):
        digit = i
        flag2 = 1
    if (flag2 == 1) and ((ord(s[i]) < 48) or (ord(s[i]) > 57)) and (flag3 == 0):
        out = out + s[i]
        ind2 = i
        rang = ind2 - ind1
        flag3 = 1
    if (flag3 == 1) and ((i - ind2) == rang):
        out = out + s[i]
        ind2 = i
        if s[i] == ".":
            break

print(f"out: {out}")
