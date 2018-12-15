from sys import stdin
from array import array

SIDE = 1100
TOTAL_SIZE = SIDE*SIDE

def parse_cut(cut):
    cut_id = cut.split('@')[0].split('#')[1].strip()

    cut_start = cut.split('@')[1].split(':')[0].strip()
    left = cut_start.split(',')[0].strip()
    top = cut_start.split(',')[1].strip()
    
    cut_area = cut.split('@')[1].split(':')[1].strip()
    width = cut_area.split('x')[0].strip()
    height = cut_area.split('x')[1].strip()
    # print(cut_id, left, ',', top, width, 'x', height)

    cut = {
        'cut_id' : cut_id,
        'cut_start' : cut_start,
        'left': int(left),
        'top': int(top),
        'cut_area': cut_area,
        'width' : int(width),
        'height' : int(height),
        }

    return cut

def mark_cut(array, cut):

    for i in range(cut['left'], cut['left'] + cut['width']):
        for j in range(cut['top'], cut['top'] + cut['height']):
            increment(array, i, j)

def peek(array, x, y, width, height):
    for j in range(y, y+height):
        for i in range(x, x+width):
            print(array[SIDE*j + i], end='')
        print()

def increment(array, x, y):
    array[SIDE*y + x] += 1

# returns true if the cut has no overlaps
def good_cut(cut, array):
    overlaps = False
    
    for i in range(cut['left'], cut['left'] + cut['width']):
        for j in range(cut['top'], cut['top'] + cut['height']):
            if not array[SIDE*j + i] == 1:
                overlaps = True

    return not overlaps
            
fabric = array('b',[0 for n in range(TOTAL_SIZE)])
cuts = list()

for row in stdin.readlines():
    cut = parse_cut(row)
    cuts.append(cut)
    mark_cut(fabric, cut)

# peek(fabric, 0,0, 20, 20)

for cut in cuts:
    if good_cut(cut,fabric):
        print(cut)
