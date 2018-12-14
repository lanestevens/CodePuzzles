serial_number = 18

def power_level(col, row, serial_number):
    rack_id = col + 10
    return ((((rack_id * row) + serial_number) * rack_id / 100) % 10) - 5

iterator = range(1, 301)
grid = [[None for col in range(301)] for row in range(301)]
for col in iterator:
    for row in iterator:
        grid[row][col] = power_level(col, row, serial_number)

current_max = None
for size in iterator: 
   for col in iterator:
        if col + size > 300:
            continue
        for row in iterator:
            if row + size > 300:
                continue
            sum_power_level = 0
            for i in range(row, row + size):
                for j in range(col, col + size):
                    sum_power_level += grid[i][j]
            if not current_max:
                current_max = (sum_power_level, col, row, size)
            elif sum_power_level > current_max[0]:
                current_max = (sum_power_level, col, row, size)
print current_max

        
