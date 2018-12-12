import sys

guard_data = sorted([x.strip() for x in sys.stdin.readlines()])

def parse_data(guard_data):
    summary = {}
    for guard_datum in guard_data:
        if 'Guard' in guard_datum:
            this_guard = int(guard_datum[guard_datum.find('#') + 1:guard_datum.find('begins') - 1])
            if this_guard not in summary:
                summary[this_guard] = [0 for x in range(60)]
        if 'falls' in guard_datum:
            sleep_start = int(guard_datum[guard_datum.find(':') + 1: guard_datum.find(']')])
        if 'wakes' in guard_datum:
            sleep_end = int(guard_datum[guard_datum.find(':') + 1: guard_datum.find(']')])
            for sleep_minute in range(sleep_start, sleep_end):
                summary[this_guard][sleep_minute] += 1
    return summary

parsed_data = parse_data(guard_data)
selected_guard = sorted([(sum(y), x) for x, y in parsed_data.items()])[-1][1]
selected_minute = sorted([(y, x) for x, y in enumerate(parsed_data[selected_guard])])[-1][1]
print selected_guard, selected_minute, selected_guard * selected_minute


