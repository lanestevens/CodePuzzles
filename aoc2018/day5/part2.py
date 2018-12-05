import sys

polymer = sys.stdin.read()
def react(unit_type,m polymer):
    polymer = polymer.replace(unit_type.lower(), '').replace(unit_type.upper())
    while True:
        changed = False
        for i in range(len(polymer) - 1):
            if polymer[i].lower() == polymer[i + 1].lower() and polymer[i].islower() != polymer[i + 1].islower():
                polymer = polymer[:i] + polymer[i + 2:]
                changed = True
                break
        if not changed:
            print unit_type, len(polymer)
            return len(polymer)

candidates = set(polymer.lower())
values = sorted([(react(x, polymer), x) for x in candidates])[0]
print values
