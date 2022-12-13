from pprint import pprint
from more_itertools import grouper

test = """
1 noop
2 addx 3
2 addx -5
""".strip().split("\n")

with open("input-modified") as f:
# with open("test") as f:
   inp = f.read().strip().split("\n")

# inp = test
ins = [l.split() for l in inp]
counter = 1
for i in ins:
    i.insert(0, counter)
    counter += int(i[1])

register = 1
for i in ins:
    i.append(register)
    if i[2] == "addx":
        register += int(i[3])


signals = []
for i in ins:
    for x in range(int(i[1])):
        signals.append({"s": (i[0]+x) * i[-1], "x": i[-1], "c": i[0]})


print("sum", sum([signals[i-1]["s"] for i in [20, 60, 100, 140, 180, 220]]))
# print("final_registerX:", register)
# 17128 too low
# 17987 too high
# 18083 not the right answer

# pprint(ins)
# pprint(list(enumerate(signals, 1)))


output = ""

for i  in ins:
    x = i[-1]
    for j in range(int(i[1])):
        cycle = i[0]+j -1
        if x-1 <= cycle % 40 <= x+1:
            output += "#"
        else:
            output += "."

print("\n".join(
    ["".join(line) for line in grouper(output, 40, incomplete='strict')]
    ))


headers = ["cycle", "ins_cycle", "op", "<operand>", "X"]
