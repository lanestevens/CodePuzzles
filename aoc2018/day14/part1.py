import sys

elf1_current = 0
elf2_current = 1
scores = [3, 7]


limit = int(sys.argv[1])
while len(scores) < limit + 10:
    combined_score = scores[elf1_current] + scores[elf2_current]
    scores = scores + [int(x) for x in list('{:d}'.format(combined_score))]
    elf1_current = (elf1_current + 1 + scores[elf1_current]) % len(scores)
    elf2_current = (elf2_current + 1 + scores[elf2_current]) % len(scores)

print ''.join(['{:d}'.format(x) for x in scores[limit:limit + 10]])


