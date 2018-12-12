import sys

def parse_step(step):
    prerequisite = step[step.find(' must') - 1]
    prerequisite_for = step[step.find(' can') - 1]
    return (prerequisite, prerequisite_for)

parsed_steps = [parse_step(x.strip()) for x in sys.stdin.readlines()]
dependencies = {}
steps = set([])

for parsed_step in parsed_steps:
    steps.add(parsed_step[0])
    steps.add(parsed_step[1])
    if parsed_step[1] in dependencies:
        dependencies[parsed_step[1]].add(parsed_step[0])
    else:
        dependencies[parsed_step[1]] = set([parsed_step[0]])

available_steps = steps.difference(set(dependencies.keys()))
result = []
while dependencies or available_steps:
    next_step = sorted(list(available_steps))[0]
    available_steps.remove(next_step)
    result.append(next_step)
    for a_step in dependencies.keys():
        dependencies[a_step].discard(next_step)
        if not dependencies[a_step]:
            available_steps.add(a_step)
            del(dependencies[a_step])
print ''.join(result)
