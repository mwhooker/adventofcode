"""

2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
For the first few pairs, this list means:

Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
The Elves in the second pair were each assigned two sections.
The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.


Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

In how many assignment pairs does one range fully contain the other?
"""


def either_fully_contained(lhs, rhs):
    """
    >>> either_fully_contained(set(range(2, 4+1)), set(range(6, 8+1)))
    False
    >>> either_fully_contained(set(range(2, 8+1)), set(range(3, 7+1)))
    True
    >>> either_fully_contained(set(range(6, 6+1)), set(range(4, 6+1)))
    True
    """
    return lhs.issubset(rhs) or lhs.issuperset(rhs)

def parse(line):
    """
    >>> tuple(sorted(x) for x in parse("2-4,6-8"))
    ([2, 3, 4], [6, 7, 8])
    >>> parse("2-2,6-6")
    ({2}, {6})
    >>> parse("22-23,666-667")
    ({22, 23}, {666, 667})
    """

    lhs, rhs = [[int(y) for y in x.split("-")] for x in line.split(",")]
    return (set(range(lhs[0], lhs[1]+1)), set(range(rhs[0], rhs[1]+1)))

if __name__ == "__main__":
    import doctest
    doctest.testmod()


with open("input") as f:
   inp = f.read().strip().split("\n")

print([either_fully_contained(*parse(line)) for line in inp].count(True))
print([set.isdisjoint(*parse(line)) for line in inp].count(False))
