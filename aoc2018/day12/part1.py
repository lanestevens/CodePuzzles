import sys

def generation(state, rules):
    buffer = '..' + state + '..'
    next_state = ''
    for i in range(2,len(state) + 2):
        pattern = buffer[i - 2:i + 3]
        if pattern in rules:
            next_state += '#'
        else:
            next_state += '.'
    return next_state

def score(state, offset):
    return sum([x[0] - offset for x in enumerate(state) if x[1] == '#'])
            
offset = 50
rows = [x.strip() for x in sys.stdin.readlines()]
state = '.'* offset + rows[0][rows[0].find(':') + 2:] + '.' * offset

rules = {x.split(' => ')[0] for x in rows if '=>' in x and x.split(' => ')[1] == '#'}

for i in range(20):
    state = generation(state, rules)
print score(state, offset)
