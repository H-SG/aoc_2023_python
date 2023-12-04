from utils import read_to_array
import time

start: time = time.perf_counter_ns()

card_dict: dict = {}

lines: list[str] = read_to_array('data/day4.txt')
total_score: int = 0
for line in lines:
    id_str, num_strs = line.split(':')

    card_id: int = int(id_str.split()[-1])

    if card_id in card_dict.keys():
        card_dict[card_id] += 1
    else:
        card_dict[card_id] = 1

    win_str, card_str = num_strs.split('|')
    win_num: list[str] = win_str.split()
    card_num: list[str] = card_str.split()

    matches: int = len(set(win_num).intersection(set(card_num)))    
    current_score: int
    if matches:
        current_score = int(2**(matches - 1))
    else:
        current_score = 0
    
    total_score += current_score

    for i in range(card_id + 1, card_id + matches + 1):
        if i in card_dict.keys():
            card_dict[i] += card_dict[card_id]
        else:
            card_dict[i] = card_dict[card_id]

print(f'Day 4 - Part 1: {total_score}')
print(f'Day 4 - Part 2: {sum(card_dict.values())}')
print(f'Loading and both solutions took {(time.perf_counter_ns() - start)/1E6:.3f} milliseconds')
