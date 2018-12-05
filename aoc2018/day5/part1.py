import sys

polymer = sys.stdin.read()
while True:
    changed = False
    for i in range(len(polymer) - 1):
        if polymer[i].lower() == polymer[i + 1].lower() and polymer[i].islower() != polymer[i + 1].islower():
            polymer = polymer[:i] + polymer[i + 2:]
            changed = True
            break
    if not changed:
        break
print len(polymer)

        
