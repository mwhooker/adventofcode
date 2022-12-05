import sys
"""

[Q]         [N]             [N]    
[H]     [B] [D]             [S] [M]
[C]     [Q] [J]         [V] [Q] [D]
[T]     [S] [Z] [F]     [J] [J] [W]
[N] [G] [T] [S] [V]     [B] [C] [C]
[S] [B] [R] [W] [D] [J] [Q] [R] [Q]
[V] [D] [W] [G] [P] [W] [N] [T] [S]
[B] [W] [F] [L] [M] [F] [L] [G] [J]
 1   2   3   4   5   6   7   8   9 

"""
_stacks = [
        "QHCTNSVB",
        "GBDW",
        "BQSTRWF",
        "NDJZSWGL",
        "FVDPM",
        "JWF",
        "VJBQNL",
        "NSQJCRTG",
        "MDWCQSJ",
        ]

def get_stacks():
    stacks = []
    for s in _stacks:
        l = list(s)
        l.reverse()
        stacks.append(l)
    return stacks


with open("input") as f:
   inp = f.read().strip().split("\n")

# 5.1
stacks = get_stacks()
for line in inp:
    _, count, _, source, _, dest = line.split()
    count, source, dest = int(count), int(source) - 1, int(dest) - 1
    for i in range(count):
        stacks[dest].append(stacks[source].pop())

print("".join(x[-1] for x in stacks))


# 5.2
stacks = get_stacks()
for line in inp:
    _, count, _, source, _, dest = line.split()
    count, source, dest = int(count), int(source) - 1, int(dest) - 1 
    stacks[source], rest = stacks[source][:-count], stacks[source][-count:]
    stacks[dest] += rest

print("".join(x[-1] for x in stacks))
