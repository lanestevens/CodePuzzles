import sys

elf1_current = 0
elf2_current = 1
scores = "37"


key = sys.argv[1]
while scores.find(key) == -1:
    combined_score = int(scores[elf1_current]) + int(scores[elf2_current])
    scores = scores + '{:d}'.format(combined_score)
    elf1_current = (elf1_current + 1 + int(scores[elf1_current])) % len(scores)
    elf2_current = (elf2_current + 1 + int(scores[elf2_current])) % len(scores)

print scores.find(key)


