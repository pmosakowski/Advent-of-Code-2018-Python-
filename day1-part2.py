import sys

adjustments = list()
for row in sys.stdin.readlines():
  adjustments.append(int(row))

freq = 0
past_freq = set()
past_freq.add(freq)


while True:

  for adjustment in adjustments:
    freq += adjustment
    if freq in past_freq:
        print(freq)
        exit()
    else:
        past_freq.add(freq)
