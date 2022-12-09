import numpy as np

with open("input") as f:
   inp = f.read().strip().split("\n")

forest = [[int(x) for x in y] for y in inp]

test = """30373
25512
65332
33549
35390""".split("\n")

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
        if any(t):
            i += 1

print(i + (2 * x_len) + (2* y_len) -4) 

# np_forest = np.genfromtxt("""30373
# 25512
# 65332
# 33549
# 35390""".split(), delimiter=1, dtype=int)

np_forest = np.genfromtxt("input", delimiter=1, dtype=int)

def cardinal_score(ar, th):
    score = 0
    for x in ar:
        score += 1
        if x >= th:
            break
    return score

def scenic_score(ar, interest):
    th = ar.item(*interest)
    a, b, c, d = (
    cardinal_score(
        ar[interest[0], :interest[1]][::-1], # left
        th
    ),
    cardinal_score(
        ar[interest[0], interest[1]+1:], # right
        th
    ),
    cardinal_score(
        ar[interest[0]+1:, interest[1]], # down
        th
    ),
    cardinal_score(
        ar[:interest[0], interest[1]][::-1], # up
        th
    )
    )

    # print("point:", interest,
    #       "val:", th,
    #       "abcd", a, b, c, d,
    #       "score:", a * b * c * d)

    return a * b * c * d

score = 0
for coord, value in np.ndenumerate(np_forest):
    # print("({}, {}) {}".format(x, y, value))
    ss = scenic_score(np_forest, coord)
    if ss > score:
        score = ss

print("ss:", score)
