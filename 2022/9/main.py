with open("input") as f:
   inp = f.read().strip().split("\n")


test = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".split("\n")

test2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".split("\n")


"""
vertical | horizontal
--------------------
ending 11 -5578
max 146 1
min -54 -5578
"""

class Head(object):
    def __init__(self, state):
        self.state = state
        self.x = self.y = 0

    def move(self, d):
        match d:
            case "D":
                self.down()
            case "U":
                self.up()
            case "L":
                self.left()
            case "R":
                self.right()
        self.state.update_head(self.x, self.y)

    def up(self):
        self.y -= 1
    def down(self):
        self.y += 1
    def left(self):
        self.x -= 1
    def right(self):
        self.x += 1


class Tail(object):

    def __init__(self, head, idx, state):
        self.x = self.y = 0
        self.head = head
        self.id = idx
        self.state = state

    def update(self):
        """
        If the head is ever two steps directly up, down, left, or right from
        the tail, the tail must also move one step in that direction so it
        remains close enough

        Otherwise, if the head and tail aren't touching and aren't in the same
        row or column, the tail always moves one step diagonally to keep up:
        """
        # import pdb; pdb.set_trace()
        dx = abs(self.x - self.head.x)
        dy = abs(self.y - self.head.y)

        if dx <= 1 and dy <= 1:
            return

        self.y = (self.y + self.head.y) // 2
        self.x = (self.x + self.head.x) // 2
        if dx + dy == 3:
            if dx == 2:
                self.y = self.head.y
            else:
                self.x = self.head.x

        s.update_tail(self.id, t.x, t.y)


class State(object):
    size = 26

    def __init__(self, tail_size):
        self.tail_states = set()
        self.tail_size = tail_size
        self.tails = [None] * tail_size
        self.update_head(0,0)
        for i in range(tail_size):
            self.update_tail(i, 0, 0)

    def update_head(self, x, y):
        self.head = (x, y)

    def update_tail(self, idx, x, y):
        self.tails[idx] = (x, y)
        if idx == 8:
            self.tail_states.add((x,y))

    def print(self):
        state = a = [["*"] * self.size for i in range(self.size)]

        for i in range(self.tail_size):
            tail = self.tails[i]
            state[tail[1] % self.size][tail[0] % self.size] = str(i+1)

        state[self.head[1] % self.size][self.head[0] % self.size] = "H"
        print("\n".join(["".join(x) for x in state]))
        print(len(self.tail_states))
        print("---")





N = 9

s = State(N)
h = Head(s)
tails = []
for i in range(N):
    if i == 0:
        tails.append(Tail(h, i, s))
    else:
        tails.append(Tail(tails[i-1], i, s))

s.print()
for line in inp:
    d, n = line.split()
    n = int(n)
    print(line)
    for i in range(n):
        h.move(d)
        for t in tails:
            t.update()
        s.print()
