num = int(input("input integer" + "\n"))
binaries = []

while num >= 1:
    div, mod = divmod(num, 2)
    binaries.insert(0, mod)
    num = div

print("".join(map(str, binaries)))
