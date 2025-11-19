n = int(input())
och = 0
zaoch = 0
for i in range(n):
    s = input().split()
    if s[3] == "True":
        och += 1
    else:
        zaoch += 1
print(f"out: {och} {zaoch}")
