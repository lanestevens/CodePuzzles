import sys

claims = [x.strip() for x in sys.stdin.readlines()]
fabric = [list('.'*1000) for x in range(1000)]

def parse_claim(claim):
    cols = int(claim[claim.find('@') + 2:claim.find(',')])
    rows = int(claim[claim.find(',') + 1:claim.find(':')])
    width = int(claim[claim.find(':') + 2: claim.find('x')])
    height = int(claim[claim.find('x') + 1:])
    return ((rows, cols), (rows + height, cols + width))
    
for claim in claims:
    claim_area = parse_claim(claim)
    for row in range(claim_area[0][0], claim_area[1][0]):
        for col in range(claim_area[0][1], claim_area[1][1]):
            fabric[row][col] = '#' if fabric[row][col] == '.' else 'X'

overlaps = 0
for row in fabric:
    for column in row:
        if column == 'X':
            overlaps += 1
print overlaps
