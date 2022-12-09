from collections import namedtuple, defaultdict
from pprint import pprint
from statemachine import StateMachine, State


class DirectoryMachine(StateMachine):
    listing = State("ls")
    changing = State("cd")

Command = namedtuple("Command", ["cmd", "output"])

class IOMachine(StateMachine):
    inputting = State('Input', initial=True)
    outputting = State('Output')

    cmd = outputting.to(inputting)
    output = inputting.to(outputting) | outputting.to(outputting)


class IOReader(object):

    cmds = []
    buffer = []
    
    def __init__(self):
        self.stm = IOMachine()

    def command(self, line):
        if self.stm.is_outputting:
            self.flush()

        self.buffer = [line]
        self.stm.output()

    def output(self, line):
        self.stm.output()
        self.buffer.append(line)

    def flush(self):
        cmd = Command(self.buffer[0], self.buffer[1:])
        self.cmds.append(cmd)


# class DirNode(object):

#     def __init__(self):
#         self.childen = []
#         self.files = []

#     def add_file(self, size):
#         self.files.append(size)




class FileTree(object):

    def __init__(self):
        self.cursor = []
        self.dirs = defaultdict(int)

    def add_file(self, size):
        tmp = []
        for i in self.cursor:
            tmp.append(i)
            self.dirs["/".join(tmp)] += size

    def cd(self, target):
        if target == "..":
            self.cursor.pop()
        else:
            self.cursor.append(target)

    def dump(self):
        s = 0
        for k in self.dirs:
            if self.dirs[k] <= 100000:
                s += self.dirs[k]
        print(s)




with open("input") as f:
   inp = f.read().strip().split("\n")


io = IOReader()
for line in inp:
    if line[0] == "$":
        io.command(line[2:])
    else:
        io.output(line)

io.flush()

ft = FileTree()

for f in io.cmds:
    if f.cmd.startswith("cd"):
        ft.cd(f.cmd.split()[1])
    for line in f.output:
        lhs, rhs = line.split() 
        if lhs != "dir":
            ft.add_file(int(lhs))
        
ft.dump()


