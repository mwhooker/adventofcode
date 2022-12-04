from more_itertools import batched, take

with open("input") as f:
   inp = f.read().strip().split("\n")


priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(sum(
    [sum([priority.index(x)+1 for x in
           set(a[0:int(len(a)/2)]).intersection(set(a[int(len(a)/2):]))])
     for a in inp]))


print(sum([priority.index(take(1, set.intersection(*map(set, a)))[0])+1 for a in
          batched(inp, 3)]))
