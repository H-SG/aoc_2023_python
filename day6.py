from dataclasses import dataclass
from utils import read_to_array
from  math import sqrt, ceil, floor
import time

start: time = time.perf_counter_ns()

lines: list[str] = read_to_array('data/day6.txt')
times: str = lines[0].split(':')[-1]
distances: str = lines[1].split(':')[-1]

@dataclass
class BoatRace():
    time_allowed: int
    distance_to_beat: int

    def __post_init__(self) -> None:
        time_1: float = (self.time_allowed + sqrt((self.time_allowed**2) - 4 * self.distance_to_beat)) / 2
        time_2: float = (self.time_allowed - sqrt((self.time_allowed**2) - 4 * self.distance_to_beat)) / 2
        self.time_range: list[int] = [ceil(min(time_1, time_2)), floor(max(time_1, time_2))]

        while self.get_distance(self.time_range[0]) <= self.distance_to_beat:
            self.time_range[0] += 1

        while self.get_distance(self.time_range[1]) <= self.distance_to_beat:
            self.time_range[1] -= 1

        self.win_options: int = self.time_range[1] - self.time_range[0] + 1

    def get_distance(self, pressed: int):
        return pressed * (self.time_allowed - pressed)

races: list[BoatRace] = []

win_options: int = 1
for t, d, in zip(times.split(), distances.split()):
    current_race: BoatRace = BoatRace(int(t), int(d))
    races.append(current_race)

    win_options *= current_race.win_options

print(f'Day 6 - Part 1: {win_options}')

big_time: int = int(times.replace(' ', ''))
big_distance: int = int(distances.replace(' ', ''))

big_race: BoatRace = BoatRace(big_time, big_distance)

print(f'Day 6 - Part 2: {big_race.win_options}')
print(f'Loading and both solutions took {(time.perf_counter_ns() - start)/1E6:.3f} milliseconds')
