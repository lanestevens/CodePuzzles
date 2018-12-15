import sys

class Cart(object):
    next_turns = {'left': 'straight',
                  'straight': 'right',
                  'right': 'left',
                  }
    next_directions = {('<', 'left'): 'v',
                       ('<', 'straight'): '<',
                       ('<', 'right'): '^',
                       ('>', 'left'): '^',
                       ('>', 'straight'): '>',
                       ('>', 'right'): 'v',
                       ('^', 'left'): '<',
                       ('^', 'straight'): '^',
                       ('^', 'right'): '>',
                       ('v', 'left'): '>',
                       ('v', 'straight'): 'v',
                       ('v', 'right'): '<',
                       }
                  
    def __init__(self, col, row, direction, track):
        self.orig_col = col
        self.orig_row = row
        self.col = col
        self.row = row
        self.direction = direction
        self.track = track
        self.next_turn = 'left'
        self.track_piece = '|' if self.direction in ('^', 'v') else '-'

        self.next_moves = {('<', '-'): lambda: '<',
                           ('<', '/'): lambda: 'v',
                           ('<', '\\'): lambda: '^',
                           ('<', '+'): self._turn,
                           ('>', '-'): lambda: '>',
                           ('>', '/'): lambda: '^',
                           ('>', '\\'): lambda: 'v',
                           ('>', '+'): self._turn,
                           ('^', '|'): lambda: '^',
                           ('^', '\\'): lambda: '<',
                           ('^', '/'): lambda: '>',
                           ('^', '+'): self._turn,
                           ('v', '|'): lambda: 'v',
                           ('v', '\\'): lambda: '>',
                           ('v', '/'): lambda: '<',
                           ('v', '+'): self._turn,
                           }
        self.moves = 0

    def _turn(self):
        next_direction = self.next_directions[(self.direction, self.next_turn)]
        self.next_turn = self.next_turns[self.next_turn]
        return next_direction
        
    def move(self):
        self.track.replace_track(self.col, self.row, self.track_piece)
        if self.direction not in ('^', 'v', '<', '>'):
            raise ValueError('Illegal direction: {:s}'.format(self.direction))
        if self.direction == '<':
            next_row = self.row
            next_col = self.col - 1
        elif self.direction == '>':
            next_row = self.row
            next_col = self.col + 1
        elif self.direction == '^':
            next_row = self.row - 1
            next_col = self.col
        else:
            next_row = self.row + 1
            next_col = self.col

        next_track_piece = self.track.get_track(next_col, next_row)
        if next_track_piece in ('v', '^', '<', '>'):
            self.track.remove_cart(next_col, next_row)
            self.track.remove_cart(self.col, self.row)
            return

        if next_track_piece == ' ':
            raise ValueError('Off track:  {:d}, {:d}, {:s}, {:d}, {:d}, {:d}'.format(self.col, self.row, self.direction, self.moves, self.orig_col, self.orig_row))
        next_direction = self.next_moves[(self.direction, next_track_piece)]()
        self.track.replace_track(next_col, next_row, next_direction)
        self.col = next_col
        self.row = next_row
        self.direction = next_direction
        self.track_piece = next_track_piece
        self.moves += 1

class Track(object):
    def __init__(self, lines, debug=False):
        self.debug = debug
        self.rows = []
        self.carts = []
        for line in lines:
            self.rows.append(list(line))
        for i in range(len(self.rows)):
            for j in range(len(self.rows[i])):
                if self.rows[i][j] in ('^', 'v', '<', '>'):
                    self.carts.append(Cart(j, i, self.rows[i][j], self))
        for cart in self.carts:
            print '{:d},{:d} {:s} {:s}'.format(cart.col, cart.row, cart.direction, cart.track_piece)
        self.print_track()

    def replace_track(self, col, row, piece):
        self.rows[row][col] = piece

    def get_track(self, col, row):
        try:
            track_piece = self.rows[row][col]
        except IndexError:
            print 'row: {:d} col: {:d}'.format(row, col)
            raise
        return track_piece

    def order_carts(self):
        self.carts = [x[2] for x in sorted([(x.row, x.col, x) for x in self.carts])]

    def remove_cart(self, col, row):
        print 'Removing cart at {:d},{:d}'.format(col, row)
        new_carts = []
        for cart in self.carts:
            if cart.col == col and cart.row == row:
                self.replace_track(cart.col, cart.row, cart.track_piece)
            else:
                new_carts.append(cart)
        self.carts = new_carts

    def tick(self):
        for cart in self.carts[:]:
            if cart in self.carts:
                cart.move()
        self.order_carts()
        self.print_track()

    def print_track(self):
        if self.debug:
            for row in self.rows:
                print ''.join(row)

track = Track([x.rstrip() for x in sys.stdin.readlines()], False)
while True:
    track.tick()
    if len(track.carts) == 1:
        print '{:d},{:d}'.format(track.carts[0].col, track.carts[0].row)
        break

