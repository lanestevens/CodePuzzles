import sys

def parse_claim(claim):
    cols = int(claim[claim.find('@') + 2:claim.find(',')])
    rows = int(claim[claim.find(',') + 1:claim.find(':')])
    width = int(claim[claim.find(':') + 2: claim.find('x')])
    height = int(claim[claim.find('x') + 1:])
    return ((rows, cols), (rows + height, cols + width), claim[1:claim.find(' ')])

def overlaps(claim1, claim2):
    if claim1[2] == claim2[2]:
        return False
    if (claim1[0][0] <= claim2[0][0] <= claim1[1][0]
        or claim1[0][0] <= claim2[1][0] <= claim1[1][0]
        or (claim2[0][0] <= claim1[0][0] and claim2[1][0] >= claim1[1][0])):
        if (claim1[0][1] <= claim2[0][1] <= claim1[1][1]
            or claim1[0][1] <= claim2[1][1] <= claim1[1][1]
            or (claim2[0][1] <= claim1[0][1] and claim2[1][1] >= claim1[1][1])):
            return True
    return False
    
claims = [parse_claim(claim) for claim in [x.strip() for x in sys.stdin.readlines()]]

for claim1 in claims:
    has_overlaps = False
    for claim2 in claims:
        if overlaps(claim1, claim2):
            has_overlaps = True
            break
    if not has_overlaps:
        print claim1

