from sys import stdin

def test(first, second):
    diff_pos = -1
    nonmatch = 0

    for i, (char_a, char_b) in enumerate(zip(first, second)):
        #print(i, char_a, char_b)
        if char_a != char_b:
            nonmatch += 1
            diff_pos = i

    return nonmatch, diff_pos
    
ids = list()

for row in stdin.readlines():
    ids.append(row.strip())
    ids = sorted(ids)

#print(ids)
pairs = list(zip(ids,ids[1:]))
#print(pairs)

for first, second in pairs:
    #print(first, second)
    nonmatch, diff = test(first, second)
    #print(nonmatch, diff)
    if nonmatch == 1:
        common = list(first)
        del common[diff]
        print("".join(common))
        exit()

