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
grid = [[None for y in range(grid_size + 1)] for x in range(grid_size + 1)]
for x in range(grid_size + 1):
    for y in range(grid_size + 1):
        for point in points.keys():
            md = manhatten_distance((x,y), point)
            if grid[x][y] is None:
                grid[x][y] = (md, point)
            elif md < grid[x][y][0]:
                grid[x][y] = (md, point)
            elif md == grid[x][y][0]:
                grid[x][y] = '.'
                break

for x in range(grid_size + 1):
    for y in range(grid_size + 1):
        if grid[x][y] == '.':
            continue
        if grid[x][y][1] in points:
            points[grid[x][y][1]] += 1

infinites = set([])
for x in (0, grid_size):
    for y in range(grid_size + 1):
        if grid[x][y] == '.':
            continue
        if grid[x][y][1] in points:
            del(points[grid[x][y][1]])
            infinites.add(grid[x][y][1])
for x in range(grid_size + 1):
    for y in (0, grid_size):
        if grid[x][y] == '.':
            continue
        if grid[x][y][1] in points:
            del(points[grid[x][y][1]])
            infinites.add(grid[x][y][1])

print sorted(points.values())[-1]
