import sys
import time

class Point(object):
    def __init__(self, col, row, vcol, vrow):
        self.col = col
        self.row = row
        self.vcol = vcol
        self.vrow = vrow

    def update(self):
        self.col += self.vcol
        self.row += self.vrow

class Grid(object):
    def __init__(self):
        self.points = []

    def add_point(self, descriptor):
        col = int(descriptor[descriptor.find('<') + 1:descriptor.find(',')])
        row = int(descriptor[descriptor.find(',') + 1:descriptor.find('>')])
        vcol = int(descriptor[descriptor.rfind('<') + 1:descriptor.rfind(',')])
        vrow = int(descriptor[descriptor.rfind(',') + 1:descriptor.rfind('>')])
        self.points.append(Point(col, row, vcol, vrow))

    def update(self):
        for point in self.points:
            point.update()
                           
    def widths(self):
        try:
            cols = sorted([x.col for x in self.points])
            return (cols[0], cols[-1])
        except:
            return None
        
    def width(self):
        widths = self.widths()
        if widths:
            return widths[1] - widths[0] + 1
        return 0

    def heights(self):
        try:
            rows = sorted([x.row for x in self.points])
            return (rows[0], rows[-1])
        except:
            return None
        
    def height(self):
        heights = self.heights()
        if heights:
            return heights[1] - heights[0] + 1
        return 0

    def col_offset(self):
        widths = self.widths()
        return -widths[0]

    def row_offset(self):
        heights = self.heights()
        return -heights[0]

    def display(self):
        height = self.height()
        width = self.width()
        if height > 32 or width > 128:
            return False

        grid = [['.' for col in range(width)] for x in range(height)]
        col_offset = self.col_offset()
        row_offset = self.row_offset()
        for point in self.points:
            grid[point.row + row_offset][point.col + col_offset] = '#'

        for row in grid:
            print ''.join(row)

        return True

grid = Grid()
for descriptor in sys.stdin.readlines():
    grid.add_point(descriptor)
    
while True:
    displayed = grid.display()
    if displayed:
        time.sleep(3)
    grid.update()

#RGRKHKNA
