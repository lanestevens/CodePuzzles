import sys

frequency = 0
frequency_changes = [int(x.strip()) for x in sys.stdin.readlines()]
seen_frequencies = set([])
done = False
while not done:
    for frequency_change in frequency_changes:
        frequency += frequency_change
        if frequency in seen_frequencies:
            done = True
            break
        seen_frequencies.add(frequency)
    
print frequency
