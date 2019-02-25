import sys
import re
from collections import defaultdict

# part one: 
# a) Find the guard that has the most minutes asleep.
# b) What minute does that guard spend asleep the most?
# c) What is the ID of the guard you chose multiplied by the minute you chose?
def part_one(data):
    guard_sleep_total = defaultdict(int)  # {<guard_id>: <total sleep in minutes>}
    guard_sleep_minutes = {}  # {<guard_id>: {<minute>: <sleep occurence counter>}}
    guard_id = 0
    sleep_start = 0

    for guard_log in data:
        time = get_time(guard_log)

        if 'begins shift' in guard_log:
            guard_id = get_guard_id(guard_log)
        elif 'falls asleep' in guard_log:
            sleep_start = time
        elif 'wakes up' in guard_log:
            guard_sleep_total[guard_id] += time - sleep_start
            guard_sleep_minutes = log_guard_sleep_minutes(guard_sleep_minutes, guard_id, sleep_start, time)
    
    guard_id_most_sleep = max(guard_sleep_total, key=guard_sleep_total.get)
    guard_minute_most_sleep = max(guard_sleep_minutes[guard_id_most_sleep], key=guard_sleep_minutes[guard_id_most_sleep].get)
    
    return guard_id_most_sleep * guard_minute_most_sleep


# part two:
# a) Of all guards, which guard is most frequently asleep on the same minute?
# b) What is the ID of the guard you chose multiplied by the minute you chose?
def part_two(data):
    guard_sleep_minutes = {}  # {<guard_id>: {<minute>: <sleep occurence counter>}}
    guard_id = 0
    sleep_start = 0

    for guard_log in data:
        time = get_time(guard_log)

        if 'begins shift' in guard_log:
            guard_id = get_guard_id(guard_log)
        elif 'falls asleep' in guard_log:
            sleep_start = time
        elif 'wakes up' in guard_log:
            guard_sleep_minutes = log_guard_sleep_minutes(guard_sleep_minutes, guard_id, sleep_start, time)
    
    max_minute_value = 0
    max_minute_key = 0
    for guard in guard_sleep_minutes:
        minute_key = max(guard_sleep_minutes[guard], key=guard_sleep_minutes[guard].get)
        minute_value = guard_sleep_minutes[guard][minute_key]
        if minute_value > max_minute_value:
            guard_id = guard
            max_minute_key = minute_key
            max_minute_value = minute_value
    
    return guard_id * max_minute_key


def get_time(log):
    return int(log.split(':')[1][:2])


def get_guard_id(log):
    return int(re.findall('#\\d*', log)[0][1:])


def log_guard_sleep_minutes(guard_sleep_minutes, guard_id, sleep_start, time):
    # initialize minute values
    if guard_id not in guard_sleep_minutes:
        guard_sleep_minutes[guard_id] = defaultdict(int)

    # increment minute values
    for i in range(sleep_start, time):
        guard_sleep_minutes[guard_id][i] += 1
    
    return guard_sleep_minutes


if __name__ == '__main__':
    data = [line.strip() for line in sys.stdin.readlines()]
    chronological_data = sorted(data, key = lambda x: re.findall('\\[.*\\]', x)[0])
    print(part_one(chronological_data))
    print(part_two(chronological_data))
