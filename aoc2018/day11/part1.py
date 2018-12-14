serial_number = 9995

def power_level(col, row, serial_number):
    rack_id = col + 10
    return ((((rack_id * row) + serial_number) * rack_id / 100) % 10) - 5

iterator = range(1, 301)
grid = [[None for col in range(301)] for row in range(301)]
for col in iterator:
    for row in iterator:
        grid[row][col] = power_level(col, row, serial_number)

results = [[0 for col in range(301)] for row in range(301)]
current_max = None
for col in iterator:
    if col > 298:
        continue
    for row in iterator:
        if row > 298:
            continue
        sum_power_level = 0
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                sum_power_level += grid[i][j]
        results[row][col] = sum_power_level
        if not current_max:
            current_max = (sum_power_level, col, row)
        elif sum_power_level > current_max[0]:
            current_max = (sum_power_level, col, row)
print current_max

        
