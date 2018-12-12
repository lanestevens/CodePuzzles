class Circle(object):
    def __init__(self, players, last_marble, debug):
        self.players = {i + 1: [] for i in range(players)}
        self.last_marble = last_marble
        self.circle = [0]
        self.current = 0
        self.marble_number = 1
        self.current_player = 1
        self.debug = debug
        self.write_state()

    def write_state(self):
        if not self.debug:
            return
        if self.marble_number == 1:
            print '[-] (0)'
        else:
            current_player = self.current_player - 1
            if current_player < 0:
                current_player = len(self.players) + 1
            msg = '[{:d}] '.format(current_player)
            for i, v in enumerate(self.circle):
                if i == self.current:
                    msg += '({:d}) '.format(v)
                else:
                    msg += '{:d} '.format(v)
            print msg

    def place_marble(self):
        self.current = (self.current + 1) % len(self.circle)
        self.current += 1
        self.circle.insert(self.current, self.marble_number)
        self.marble_number += 1

    def remove_marble(self):
        for i in range(7):
            self.current -= 1
            if self.current < 0:
                self.current = len(self.circle) - 1
        marble = self.circle.pop(self.current)
        return marble

    def play(self):
        while self.marble_number <= self.last_marble:
            if self.marble_number % 23 == 0:
                self.players[self.current_player].append(self.marble_number)
                self.players[self.current_player].append(self.remove_marble())
                self.marble_number += 1
            else:
                self.place_marble()
            self.current_player += 1
            if self.current_player not in self.players:
                self.current_player = 1
            self.write_state()

    def winner(self):
        return sorted([sum(x) for x in self.players.values()])[-1]

data = ((10, 1618, 8317),
        (13, 7999, 146373),
        (17, 1104, 2764),
        (21, 6111, 54718),
        (30, 5807, 37305),
        )
for players, last_marble, expected in data:
    c = Circle(players, last_marble, False)
    c.play()
    if c.winner() != expected:
        print players, last_marble, expected, c.winner()

c = Circle(468, 71010, False)
c.play()
print c.winner()
