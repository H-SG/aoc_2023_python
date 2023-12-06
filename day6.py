from  math import sqrt, ceil, floor
import time

start: time = time.perf_counter_ns()

times: list[int] = [52, 94, 75, 94]
distances: list[int] = [426, 1374, 1279, 1216]

def get_win_options(time: int, distance_to_beat: int) -> int:
    root: float = sqrt((time**2) - 4 * (distance_to_beat + 1))
    t0: float = (time + root) / 2
    t1: float = (time - root) / 2

    return floor(t0) - ceil(t1) + 1

win_options: int = 1
for t, d, in zip(times, distances):    
    win_options *= get_win_options(int(t), int(d))

big_time: int = int("".join([str(x) for x in times]))
big_distance: int = int("".join([str(x) for x in distances]))

print(win_options)
print(get_win_options(big_time, big_distance))

end_ns = (time.perf_counter_ns() - start)/1E6
print(f'Loading and both solutions took {end_ns} milliseconds')
