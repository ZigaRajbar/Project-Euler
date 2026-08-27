fakulteta = 1

for i in range(1, 101):
    fakulteta = fakulteta * i

vsota = 0

for stevka in str(fakulteta):
    vsota = vsota + int(stevka)

print(vsota)
