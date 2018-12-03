import sys
import itertools

box_ids = [x.strip() for x in sys.stdin.readlines()]
def compare(s1, s2):
    return len([(x, y) for x, y in zip(s1, s2) if x != y])

for s1, s2 in itertools.combinations(box_ids, 2):
    if compare(s1, s2) == 1:
        print ''.join([x for x, y in zip(s1, s2) if x == y])



