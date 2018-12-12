import sys

coordinates = [x.strip() for x in sys.stdin.readlines()]

def manhatten_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

points = {}
max_x = 0
max_y = 0
for coordinate in coordinates:
    x, y = [int(x.strip()) for x in coordinate.split(',')]
    points[(x,y)] = 0
    max_x = max(x, max_x)
    max_y = max(y, max_y)

grid_size = max(max_x, max_y)
grid = [[0 for y in range(grid_size + 1)] for x in range(grid_size + 1)]
for x in range(grid_size + 1):
    for y in range(grid_size + 1):
        md = sum([manhatten_distance((x,y), p) for p in points.keys()])
        if md < 10000:
            grid[x][y] = 1

print sum([sum(x) for x in grid])
