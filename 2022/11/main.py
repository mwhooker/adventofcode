


def make_monkey(s):
    i = """Monkey 1:
  Starting items: 58, 93, 88, 81, 72, 73, 65
  Operation: new = old + 2
  Test: divisible by 7
    If true: throw to monkey 6
    If false: throw to monkey 7"""



class Monkey(object):
    def __init__(self, id_, items, operation, test):
        self.id = id_
        self.inspection_count = 0
        self.items = items
        self.operation = operation
        self.test = test

