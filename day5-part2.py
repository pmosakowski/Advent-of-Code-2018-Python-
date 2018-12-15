from sys import stdin
from itertools import count

def reduction(polymer):
    length_before = len(polymer)
    polymer = reduce_pass(polymer)
    length_after = len(polymer)

    while length_after < length_before:
        length_before = len(polymer)
        polymer = reduce_pass(polymer)
        length_after = len(polymer)
        
    return polymer
    
def matches(a, b):
    return a != b and a.lower() == b.lower()
    
def reduce_pass(polymer):
    rev_polymer = list(reversed(polymer))
    length = len(polymer)
    
    pairs = zip(rev_polymer[:-1], rev_polymer[1:], range(length-1,-1,-1), range(length-2,-1,-1))
    skip_next = False

    for pair in pairs:
        if not skip_next and matches(pair[0], pair[1]):
            # print(pair)

            # has to be done in reverse
            del polymer[pair[2]]
            del polymer[pair[3]]
            
            skip_next = True
        else:
            skip_next = False

    return polymer

polymer = list(stdin.readline().strip())

units = {unit.lower() for unit in polymer}

shortest_length = len(polymer)

for unit in units:
    
    print(unit)
    filtered_polymer = [u for u in polymer if u.lower() != unit]

    reduced_polymer = reduction(filtered_polymer)

    if len(reduced_polymer) < shortest_length:
        shortest_length = len(reduced_polymer)
        chosen_unit = unit

print(chosen_unit, shortest_length)


