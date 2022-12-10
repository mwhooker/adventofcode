with open("input") as f:
   inp = f.read().strip().split("\n")



vertical = horizontal = 1

vs, hs = [], []

for line in inp:
    d, n = line.split()
    n = int(n)
    match d:
        case "D":
            vertical -= n
        case "U":
            vertical += n
        case "L":
            horizontal -= n
        case "R":
            horizontal -= n
    vs.append(vertical)
    hs.append(horizontal)

print(vs)
print("ending", vertical, horizontal)
print("max", max(vs), max(hs))
print("min", min(vs), min(hs))

