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
            
iteration_limit = 50000000000
iterations = 0
offset = 0
rows = [x.strip() for x in sys.stdin.readlines()]
state = rows[0][rows[0].find(':') + 2:]
if state[0] == '#':
    state = '..' + state
    offset += 2
elif state[1] == '#':
    state = '.' + state
    offset += 1
    
if state[-1] == '#':
    state = state + '..'
elif state[-2] == '#':
    state = state + '.'

rules = {x.split(' => ')[0] for x in rows if '=>' in x and x.split(' => ')[1] == '#'}
seen_values = {state}
print_state = 0
while iterations < iteration_limit:
    state = generation(state, rules)
    if state[0] == '#':
        state = '..' + state
        offset += 2
    elif state[1] == '#':
        state = '.' + state
        offset += 1
    while state[2] == '.':
        state = state[1:]
        offset -= 1
        
    if state[-1] == '#':
        state = state + '..'
    elif state[-2] == '#':
        state = state + '.'
    iterations += 1
    if print_state or state in seen_values:
        print score(state, offset - (iteration_limit - iterations))
        break
        print iterations, offset
        print_state += 1

    if print_state > 10:
        break
    seen_values.add(state)
    if (iterations % 1000) == 0:
        if not old_state:
            old_state = state
        print iterations, len(state), offset, score(state, offset), old_state == state
        old_state = state
