from utils import read_to_array

lines: list[str] = read_to_array('data/day2.txt')
red_balls: int = 12
green_balls: int = 13
blue_balls: int = 14
id_sum: int = 0
power_sum: int = 0

for line in lines:
    # maybe I don't need to use all these strips, maybe I'm lazy and it's a saturday morning
    id: int = int(line.split(':')[0].strip().split(' ')[-1].strip())
    valid: bool = True
    rounds: str = line.split(':')[-1].strip()

    red: int = 0
    green: int = 0
    blue: int = 0

    for round in rounds.split(';'):
        for balls in round.strip().split(','):
            match balls.strip().split(' '):
                case [val, 'red']:
                    red = max(red, int(val))
                case [val, 'green']:
                    green = max(green, int(val))
                case [val, 'blue']:
                    blue = max(blue, int(val))

    if red > red_balls:
        valid = False
    if green > green_balls:
        valid = False
    if blue > blue_balls:
        valid = False

    if valid:
        id_sum += id

    power_sum += red * green * blue
                
print(f'Day 2 - Part 1: {id_sum}')
print(f'Day 2 - Part 2: {power_sum}')
