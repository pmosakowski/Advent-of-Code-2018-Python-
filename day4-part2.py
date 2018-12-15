from sys import stdin
import re
from array import array


def get_order(match):
    return int(match.group(1)) * 100000000 +\
           int(match.group(2)) * 1000000 +\
           int(match.group(3)) * 10000 +\
           int(match.group(4)) * 100 +\
           int(match.group(5))

def parse_events():
    events = list()
    
    for row in stdin.readlines():
        record = '\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (?P<event>[\S+ ]+)'
        
        match = re.match(record, row)
        event = {
            #'order' : 0,
            'order' : get_order(match),
            'name': match.group('event'),
            'minutes': int(match.group(5)),
            }

        events.append(event)

    return events

def process_events(events):
    begin = 'Guard #(\d+) begins shift'
    asleep = 'falls asleep'
    awake = 'wakes up'
    
    guards = dict()
    
    current_guard = -1
    guard_asleep = -1
    guard_awake = -1
    
    for event in events:
        name = event['name']
        minutes = event['minutes']
        match = re.match(begin, name)

        if match:
            guard_id = int(match.group(1))
            if guard_id not in guards:
                guard = {
                    'id': guard_id,
                    'minutes': array('b', [0 for n in range(60)])
                }

                guards[guard_id] = guard

            current_guard = guard_id
            continue

        match = re.match(asleep, name)

        if match:
            guard_asleep = minutes
            continue

        match = re.match(awake, name)

        if match:
            guard_awake = minutes

            minutes = guards[current_guard]['minutes']
            for i in range(guard_asleep, guard_awake):
                minutes[i] += 1

            guards[current_guard]['minutes'] = minutes

    return guards

def find_minute(guard):
    most = max(guard['minutes'])
    return most, guard['minutes'].index(most), guard['id']

def find_sleepiest_minute(guards):
    return [find_minute(g) for g in guards.values()]

events = parse_events()

#for event in events:
#    print(event)

events.sort(key=lambda event: event['order'])

#for event in events:
#    print(event)
    
guards = process_events(events)

#for guard in guards:
#    print("".join([str(i) for i in guards[guard]['minutes']]))

# sleepiest_guard = find_sleepiest(guards)
# print(sleepiest_guard)

# minute = find_minute(guards[sleepiest_guard])
# print(minute)

minutes = find_sleepiest_minute(guards)
minutes.sort(key=lambda minute: minute[0], reverse=True)
minute = minutes[0]
print(minute[1] * minute[2])
