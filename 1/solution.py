with open("input") as f:
    inp = f.read()
cals = list(map(lambda x: sum(map(int, x.split("\n"))), inp.split("\n\n")[:-1]))


# 1

max(cals)

# 2

 sum(sorted(cals)[-3:])
