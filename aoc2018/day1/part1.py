import sys

start = 0
for line in sys.stdin.readlines():
    start += int(line.strip())
print start

