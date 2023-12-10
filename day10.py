from utils import read_to_array
import time

start: time = time.perf_counter_ns()

pipelines: list[str] = read_to_array('data/day10.txt')

pipe_dict: dict = {}

for y, pipeline in enumerate(pipelines):
    for x, pipe in enumerate(pipeline):
        match pipe:
            case '|':
                pipe_dict[(x, y)] = [(x, y - 1), (x, y + 1), '║']
            case '-':
                pipe_dict[(x, y)] = [(x - 1, y), (x + 1, y), '═']
            case 'L':
                pipe_dict[(x, y)] = [(x, y - 1), (x + 1, y), '╚']
            case 'J':
                pipe_dict[(x, y)] = [(x, y - 1), (x - 1, y), '╝']
            case '7':
                pipe_dict[(x, y)] = [(x - 1, y), (x, y + 1), '╗']
            case 'F':
                pipe_dict[(x, y)] = [(x, y + 1), (x + 1, y), '╔']
            case 'S':
                starting_point: tuple[int] = (x, y)
                coords: list[tuple] = []
                charmap: list[bool] = [False, False, False, False] # N E W S

                if y - 1 >= 0:
                    if pipelines[y - 1][x] in ['|', '7', 'F']:
                        coords.append((x, y - 1))
                        charmap[0] = True


                if y + 1 < len(pipelines):
                    if pipelines[y + 1][x] in ['|', 'J', 'L']:
                        coords.append((x, y + 1))
                        charmap[3] = True
                
                if x + 1 < len(pipeline):
                    if pipelines[y][x + 1] in ['-', 'J', '7']:
                        coords.append((x + 1, y))
                        charmap[1] = True

                if x - 1 >= 0:
                    if pipelines[y][x - 1] in ['-', 'F', 'L']:
                        coords.append((x - 1, y))
                        charmap[2] = True

                match charmap:
                    case [True, False, True, False]:
                        coords.append('╝')
                    case [True, True, False, False]:
                        coords.append('╚')
                    case [False, False, True, True]:
                        coords.append('╗')
                    case [False, True, False, True]:
                        coords.append('╔')
                    case [True, False, False, True]:
                        coords.append('║')
                    case [False, True, True, False]:
                        coords.append('═')

                pipe_dict[(x, y)] = coords
            case _:
                continue

next_point: tuple[int] = pipe_dict[starting_point][0]
prev_point: tuple[int] = starting_point
steps: int = 1
travelled: list[tuple] = [starting_point]

while next_point != starting_point:
    travelled.append(next_point)
    next_points = pipe_dict[next_point]    

    if next_points[0] == prev_point:
        prev_point = next_point      
        next_point = next_points[1]
    else:
        prev_point = next_point
        next_point = next_points[0]

    steps += 1

print(f"Day 10 - Part 1: {int(steps/2)}")

# part 2
def check_point_in_polygon(line: str) -> bool:
    # https://en.wikipedia.org/wiki/Jordan_curve_theorem#Application
    edge_chars: str = line.replace(' ', '').replace('.', '').replace('═', '').replace('╚╝', '').replace('╔╗', '').replace('╚╗', '║').replace('╔╝', '║')

    return bool(len(edge_chars) % 2)

new_map: list[list[str]] = [['.' for x in range(len(pipelines[0]))] for y in range(len(pipelines))]

for travel in travelled:
    new_map[travel[1]][travel[0]] = pipe_dict[travel][-1]

inside_points: int = 0
for y, line in enumerate(new_map):
    for x in range(len(line)):
        if line[x] == '.' :
            if check_point_in_polygon("".join(line[:x + 1])):
                inside_points += 1
            else:
                new_map[y][x] = ' '

print(f'Day 10 - Part 2: {inside_points}')
print(f'Loading and both solutions took {(time.perf_counter_ns() - start)/1E6:.3f} milliseconds')

with open('data/day10_map.txt', 'w') as f:
    for line in new_map:
        f.write(f'{"".join(line)}\n') 
