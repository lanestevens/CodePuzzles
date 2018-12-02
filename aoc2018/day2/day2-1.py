import sys

box_ids = [x.strip() for x in sys.stdin.readlines()]
twos = 0
threes = 0
for box_id in box_ids:
    candidates = set(box_id)
    for candidate in candidates:
        if box_id.count(candidate) == 2:
            twos += 1
            break
    for candidate in candidates:
        if box_id.count(candidate) == 3:
            threes += 1
            break
print twos * threes
