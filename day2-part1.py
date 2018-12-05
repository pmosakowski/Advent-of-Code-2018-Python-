from sys import stdin

def test_count(box_id):
    double = 0
    triple = 0
    
    letters = list(box_id)
    ordered = sorted(letters)

    counts = dict()

    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    totals = counts.values()

    if 2 in totals:
        double = 1
    if 3 in totals:
        triple = 1

    return double, triple

total_doubles = 0
total_triples = 0
    
for row in stdin.readlines():
    doubles, triples = test_count(row.strip())

    total_doubles += doubles
    total_triples += triples

print(total_doubles*total_triples)


