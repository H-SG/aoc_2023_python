from utils import read_to_array
from math import lcm
import time

start: time = time.perf_counter_ns()

lines: list[str] = read_to_array('data/day8.txt')

instructions: str = lines[0]
current_nodes: list[str] = []
step_counts: list[int] = []

left_nodes: dict = {}
right_nodes: dict = {}
end_dict: dict = {}

current_pos: str = 'AAA'

for line in lines[2:]:
    node: str = line.split('=')[0].strip()
    directions: list[str] = line.split('=')[1].strip()[1:-1].split(',')

    left_nodes[node] = directions[0].strip()
    right_nodes[node] = directions[1].strip()

    if node[-1] == 'A':
        current_nodes.append(node)

    if node[-1] == 'Z':
        end_dict[node] = True
    else:
        end_dict[node] = False

def get_steps_to_part1_end(current_pos: str) -> int:
    step_count: int = 0
    while current_pos != 'ZZZ':
        for instruction in instructions:
            match instruction:
                case 'L':
                    current_pos = left_nodes[current_pos]
                case 'R':
                    current_pos = right_nodes[current_pos]

            step_count += 1
            if current_pos == 'ZZZ':
                break

    return step_count

def get_steps_to_part2_end(current_pos: str) -> int:
    step_count: int = 0
    while current_pos[-1] != 'Z':
        for instruction in instructions:
            match instruction:
                case 'L':
                    current_pos = left_nodes[current_pos]
                case 'R':
                    current_pos = right_nodes[current_pos]

            step_count += 1
            if current_pos[-1] == 'Z':
                break

    return step_count

print(f'Day 8 - Part 1: {get_steps_to_part1_end(current_pos)}')

for current_node in current_nodes:
    step_counts.append(get_steps_to_part2_end(current_node))

print(f'Day 8 - Part 2: {lcm(*step_counts)}')
print(f'Loading and both solutions took {(time.perf_counter_ns() - start)/1E6:.3f} milliseconds')