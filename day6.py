from utils import read_to_array
from  math import sqrt, ceil, floor
import time

start: time = time.perf_counter_ns()

lines: list[str] = read_to_array('data/day6.txt')
times: str = lines[0].split(':')[-1]
distances: str = lines[1].split(':')[-1]

def get_win_options(time: int, distance_to_beat: int) -> int:
    t0: float = (time + sqrt((time**2) - 4 * (distance_to_beat + 1))) / 2
    t1: float = (time - sqrt((time**2) - 4 * (distance_to_beat + 1))) / 2

    return abs(ceil(min(t0, t1)) - floor(max(t0, t1))) + 1

win_options: int = 1
for t, d, in zip(times.split(), distances.split()):    
    win_options *= get_win_options(int(t), int(d))

print(f'Day 6 - Part 1: {win_options}')

big_time: int = int(times.replace(' ', ''))
big_distance: int = int(distances.replace(' ', ''))

print(f'Day 6 - Part 2: {get_win_options(big_time, big_distance)}')
print(f'Loading and both solutions took {(time.perf_counter_ns() - start)/1E6:.3f} milliseconds')
