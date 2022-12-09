with open("input") as f:
   inp = f.read().strip().split("\n")

forest = [[int(x) for x in y] for y in inp]

test = """30373
25512
65332
33549
35390""".split("\n")
print("\n".join(test))

# forest = test

def visible_left(y, x):
    return len([a for a in forest[y][:x] if a >= forest[y][x]]) == 0

def visible_right(y, x):
    return len([a for a in forest[y][x+1:] if a >= forest[y][x]]) == 0

def visible_top(y, x):
    return len([a for a in [b[x] for b in forest[:y]] if a >=
                forest[y][x]]) == 0

def visible_bottom(y, x):
    return len([a for a in [b[x] for b in forest[y+1:]] if a >=
                forest[y][x]]) == 0


i = 0

y_len = len(forest)
x_len = len(forest[0])

for y in range(y_len):
    for x in range(x_len):
        if y == 0 or x == 0 or y +1 == y_len or x + 1 == x_len:
            continue
        t = (
                visible_left(y, x),
                visible_right(y, x),
                visible_top(y, x),
                visible_bottom(y, x)
                )
        print(t)
        if any(t):
            i += 1
            print("True",)
        else:
            print("False",)
    print("")

print(i)
print(i + (2 * x_len) + (2* y_len) -4) 

# 9409 too high
# 9035 too high

# 3696 is wrong

# 1731 too low
