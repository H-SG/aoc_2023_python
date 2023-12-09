from utils import read_to_array
from itertools import pairwise
import time

start: time = time.perf_counter_ns()

sequences: list[str] = read_to_array('data/day9.txt')

next_value_sum: int = 0
previous_value_sum: int = 0
for sequence in sequences:
    numbers = [int(x) for x in sequence.split()]
    last_numbers: list[int] = [numbers[-1]]
    first_numbers: list[int] = [numbers[0]]

    while any(numbers):
        numbers = [y - x for x, y in pairwise(numbers)]
        last_numbers.append(numbers[-1])
        first_numbers.append(numbers[0])

    next_value_sum += sum(last_numbers)

    first_numbers.reverse()
    new_first: int = first_numbers[0]

    for first_number in first_numbers[1:]:
        new_first = first_number - new_first

    previous_value_sum += new_first

print(f'Day 9 - Part 1: {next_value_sum}')
print(f'Day 9 - Part 2: {previous_value_sum}')
print(f'Loading and both solutions took {(time.perf_counter_ns() - start)/1E6:.3f} milliseconds')