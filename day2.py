from dataclasses import dataclass
from utils import read_to_array

@dataclass
class Game():
    id: int
    red_count: int = 0
    green_count: int = 0
    blue_count: int = 0

    def check_validity(self, r: int, g: int, b: int) -> None:
        self.valid: bool = True
        if self.red_count > r:
            self.valid = False

        if self.green_count > g:
            self.valid = False

        if self.blue_count > b:
            self.valid = False

    def calc_power(self) -> None:
        self.power: int = self.red_count * self.blue_count * self. green_count

lines = read_to_array('data/day2.txt')

red_balls = 12
green_balls = 13
blue_balls = 14

games = []
id_sum = 0
power_sum = 0

for line in lines:
    # maybe I don't need to use all these strips, maybe I'm lazy and it's a saturday morning
    id = int(line.split(':')[0].strip().split(' ')[-1].strip())
    rounds = line.split(':')[-1].strip()

    games.append(Game(id))

    for round in rounds.split(';'):
        for balls in round.strip().split(','):
            match balls.strip().split(' '):
                case [val, 'red']:
                    games[-1].red_count = max(games[-1].red_count, int(val))
                case [val, 'green']:
                    games[-1].green_count = max(games[-1].green_count, int(val))
                case [val, 'blue']:
                    games[-1].blue_count = max(games[-1].blue_count, int(val))

    games[-1].check_validity(red_balls, green_balls, blue_balls)
    games[-1].calc_power()

    if games[-1].valid:
        id_sum += games[-1].id

    power_sum += games[-1].power
                
print(f'Day 2 - Part 1: {id_sum}')
print(f'Day 2 - Part 2: {power_sum}')
