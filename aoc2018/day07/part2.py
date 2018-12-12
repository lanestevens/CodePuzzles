import sys

class Worker(object):
    def __init__(self, task_overhead):
        self.task_overhead = task_overhead
        self.work_load = 0
        self.task = None

    def is_available(self):
        return self.work_load == 0
        
    def assign_task(self, task):
        self.work_load = ord(task) - 64 + self.task_overhead
        self.task = task

    def second(self):
        if self.work_load:
            self.work_load -= 1

    def complete_task(self):
        if self.work_load == 0 and self.task:
            this_task = self.task
            self.task = None
            return this_task
        return None
        
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
additional_time = 60
staff = 5
workers = [Worker(additional_time) for x in range(staff)]
seconds = 0

while dependencies or available_steps or [x for x in workers if not x.is_available()]:
    for task in sorted(list(available_steps)):
        for worker in workers:
            if worker.is_available():
                worker.assign_task(task)
                available_steps.remove(task)
                break
    for worker in workers:
        worker.second()
        task = worker.complete_task()
        if task:
            for a_step in dependencies.keys():
                dependencies[a_step].discard(task)
                if not dependencies[a_step]:
                    available_steps.add(a_step)
                    del(dependencies[a_step])
            
    seconds += 1
print seconds
