m = int(input("Минуты:"))
hh = (m // 60) % 24
mm = m % 60
print(f"{hh}:{mm}")
