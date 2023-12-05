from utils import read_to_array
from dataclasses import dataclass
from itertools import batched
import time

start: time = time.perf_counter_ns()

lines: list[str] = read_to_array('data/day5.txt')

index_list: list[list] = []

index_strings = [
    "seed-to-soil map:",
    "soil-to-fertilizer map:",
    "fertilizer-to-water map:",
    "water-to-light map:",
    "light-to-temperature map:",
    "temperature-to-humidity map:",
    "humidity-to-location map:"
]

@dataclass
class GardenMap():
    id: int
    input_start: list[int]
    output_start: list[int]
    range: list[int]

    def __post_init__(self) -> None:
        self.diff: list[int] = []
        for s, d in zip(self.input_start, self.output_start):
            self.diff.append(d - s)


    def get_output_from_input(self, input: int) -> int:
        for i, r, d in zip(self.input_start, self.range, self.diff):
            if input >= i:
                if input < i + r:
                    return input + d
                
        return input
    
    def get_input_from_output(self, output: int) -> int:
        for i, o, r, d in zip(self.input_start, self.output_start, self.range, self.diff):
            if output >= o:
                if output < o + r:
                    if output - d >= i:
                        if output - d < i + r: 
                            return output - d
                
        return output
    
    def get_output_ranges_from_input_ranges(self, inputs: list[list[int]]) -> list[list[int]]:
        output: list[list[int]] = []
        current_inputs: list[list[int]] = inputs
        while True:
            for input in current_inputs:
                current_lower: int = input[0]
                current_upper: int = input[1]
                for i, r, d in zip(self.input_start, self.range, self.diff):
                    input_start: int = i
                    input_end: int  = i + r - 1

                    if current_lower > input_end:
                        continue

                    if current_upper < input_start:
                        continue

                    # input is subset of start range - CHECKED
                    if (current_lower >= input_start) and (current_upper <= input_end):
                        output.append([current_lower + d, current_upper + d])
                        del current_inputs[current_inputs.index(input)]
                        break

                    # input is right of start range - CHECKED
                    if current_lower >= input_start:
                        output.append([current_lower + d, input_end + d])
                        del current_inputs[current_inputs.index(input)]
                        current_inputs.append([i + r, current_upper])                     
                        break


                    # input is left set of start range - CHECKED
                    if current_upper <= input_end:
                        output.append([i + d, current_upper + d])
                        del current_inputs[current_inputs.index(input)]
                        current_inputs.append([current_lower, i - 1])
                        break

                    # input is a superset of start range - CHECKED
                    output.append([i + d, input_end + d])
                    del current_inputs[current_inputs.index(input)]
                    current_inputs.append([current_lower, i - 1])
                    current_inputs.append([i + r, current_upper])
                    break


                else:
                    # input is not overlapping with any start ranges - CHECKED
                    output.append([current_lower, current_upper])
                    del current_inputs[current_inputs.index(input)]

            if len(current_inputs) == 0:
                break

        return output

def parse_to_class(id: int, lines: list[str]) -> GardenMap:
    sources: list[int] = []
    destinations: list[int] = []
    ranges: list[int] = []

    for line in lines:
        sources.append(int(line.split()[1]))
        destinations.append(int(line.split()[0]))
        ranges.append(int(line.split()[2]))

    return GardenMap(id, sources, destinations, ranges)


for i, line in enumerate(lines):
    if 'seeds:' in line:
        seeds: list[int] = [int(x) for x in line.split(':')[-1].split()]

    for index_string in index_strings:
        if index_string in line:
            if len(index_list) > 0:
                index_list[-1][1] = i - 1
            index_list.append([i + 1, 0])
            break

index_list[-1][1] = len(lines) + 1

seed2soil: GardenMap = parse_to_class(0, lines[index_list[0][0]:index_list[0][1]])
soil2fert: GardenMap = parse_to_class(1, lines[index_list[1][0]:index_list[1][1]])
fert2water: GardenMap = parse_to_class(2, lines[index_list[2][0]:index_list[2][1]])
water2light: GardenMap = parse_to_class(3, lines[index_list[3][0]:index_list[3][1]])
light2temp: GardenMap = parse_to_class(4, lines[index_list[4][0]:index_list[4][1]])
temp2hum: GardenMap = parse_to_class(5, lines[index_list[5][0]:index_list[5][1]])
hum2loc: GardenMap = parse_to_class(6, lines[index_list[6][0]:index_list[6][1]])

map_list: list[GardenMap] = [seed2soil, soil2fert, fert2water, water2light, light2temp, temp2hum, hum2loc]

locations: list[int] = []
for seed in seeds:
    input: int = seed
    for maps in map_list:
        input = maps.get_output_from_input(input)

    locations.append(input)

print(f'Day 5 - Part 1: {min(locations)}')

outputs: list[list[int]] = []

for seed_range in batched(seeds, 2):
    inputs: list[list[int]] = [[seed_range[0], seed_range[0] + seed_range[1] - 1]]
    
    for maps in map_list:
        inputs = maps.get_output_ranges_from_input_ranges(inputs)
    outputs.append(inputs)


def get_min_nested_lists(input: list) -> int:
    return min(x if isinstance(x, int) else get_min_nested_lists(x) for x in input)

print(f'Day 5 - Part 2: {get_min_nested_lists(outputs)}')
print(f'Loading and both solutions took {(time.perf_counter_ns() - start)/1E6:.3f} milliseconds')
