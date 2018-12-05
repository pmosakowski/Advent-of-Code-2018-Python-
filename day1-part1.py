import sys

total = 0

for row in sys.stdin.readlines():
    total += int(row)

print(total)
