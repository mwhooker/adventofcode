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


"""
vertical | horizontal
--------------------
ending 11 -5578
max 146 1
min -54 -5578
"""

class Head(object):
    def __init__(self):
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

    def up(self):
        self.y -= 1
    def down(self):
        self.y += 1
    def left(self):
        self.x -= 1
    def right(self):
        self.x += 1

class Tail(object):
    def __init__(self, head):
        self.x = self.y = 0
        self.head = head


    def update(self, head):
        """
        If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:
        Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:
        """
        # import pdb; pdb.set_trace()
        dx = abs(self.x - self.head.x)
        dy = abs(self.y - self.head.y)

        if dx <= 1 and dy <= 1:
            return

        # TODO: doesn't do diagonals correctly.
        """
        ......        ......
        ....T.        ....T.
        ......   ->   ....H.
        ...H..        ......
        s.....        s.....
        """
        self.y = (self.y + self.head.y) // 2
        self.x = (self.x + self.head.x) // 2
        if dx + dy == 3:
            if dx == 2:
                self.y = self.head.y
            else:
                self.x = self.head.x






class State(object):
    size = 6
    def __init__(self):
        self.head = (0,0)
        self.tail = (0,0)

    def update_head(self, x, y):
        self.head = (x, y)

    def update_tail(self, x, y):
        self.tail = (x, y)

    def print(self):
        state = [['*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*']]

        state[self.tail[1] % self.size][self.tail[0] % self.size] = "T"
        state[self.head[1] % self.size][self.head[0] % self.size] = "H"
        print("\n".join(["".join(x) for x in state]))
        print("---")





h = Head()
t = Tail(h)
s = State()

s.print()
for line in test:
    d, n = line.split()
    n = int(n)
    print(line)
    for i in range(n):
        h.move(d)
        t.update(h)
        s.update_head(h.x, h.y)
        s.update_tail(t.x, t.y)
        s.print()
