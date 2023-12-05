from utils import read_to_array
from dataclasses import dataclass
from itertools import batched
from typing import Optional
import re

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

seed_i: int
seed2soil_i: int
soil2fert_i: int
fert2water_i: int
water2light: int
light2temp: int
temp2hum: int
hum2loc: int

@dataclass
class GardenMap():
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
    
    def get_input_ranges_from_output_ranges(self, output_ranges: list[int]) -> list[list[int]]:
        input_ranges: list[list[int]] = []
        new_output_ranges: list[list[int]] = output_ranges

        while True:            
            for output_range in new_output_ranges:
                current_lower: int = output_range[0]
                current_higher: int = output_range[1]
                for i, o, r, d in zip(self.input_start, self.output_start, self.range, self.diff):
                    if current_higher < o:
                        continue

                    if current_lower > o + r:
                        continue

                    # if the ranges match exactly
                    if (current_lower == o) and (current_higher == o + r):
                        input_ranges.append([i, i + r])
                        del new_output_ranges[new_output_ranges.index(output_range)]
                        break

                    # if the range is a full subset
                    if (current_lower > o) and (current_higher < o + r):
                        input_ranges.append([current_lower - d, current_higher - d])
                        del new_output_ranges[new_output_ranges.index(output_range)]
                        new_output_ranges.append([o, current_lower - 1])
                        new_output_ranges.append([current_higher + 1, o + r])
                        break

                    # if the output is a full subet
                    if (current_lower < o) and (current_higher > o + r):
                        input_ranges.append([o - d, o + r - d])
                        del new_output_ranges[new_output_ranges.index(output_range)]
                        new_output_ranges.append([o, current_lower - 1])
                        new_output_ranges.append([current_higher + 1, o + r])
                        break

                    # if the range is a partial left set
                    if (current_higher < o + r):
                        input_ranges.append([current_lower - d, current_higher - d])
                        del new_output_ranges[new_output_ranges.index(output_range)]
                        new_output_ranges.append([current_higher + 1, o + r])
                        break

                    # if the range is a partial right set
                    if (current_lower > 0):
                        input_ranges.append([current_lower - d, current_higher - d])
                        del new_output_ranges[new_output_ranges.index(output_range)]
                        new_output_ranges.append([o, current_lower - 1])
                        break
                else:
                    input_ranges.append([current_lower, current_higher])
                    del new_output_ranges[new_output_ranges.index(output_range)]

            if len(new_output_ranges) == 0:
                return input_ranges



    def get_min_output_inputs(self) -> int:
        input_ranges: list[list] = []
        min_output_dest: int = min(self.output_start)
        source_threshold: int = min(self.input_start) - 1

        if source_threshold >= 0:
            if source_threshold < min_output_dest:
                return [0, source_threshold]
        else:
            return -1


    
    def get_upper_min_output(self) -> int:
        min_source: int = min(self.input_start)
        min_dest: int = min(self.output_start)
        if min_dest > min_source:
            return min_source - 1
        else:
            return self.input_start[self.output_start.index(min_dest)]


def parse_to_class(lines: list[str]) -> GardenMap:
    sources: list[int] = []
    destinations: list[int] = []
    ranges: list[int] = []

    for line in lines:
        sources.append(int(line.split()[1]))
        destinations.append(int(line.split()[0]))
        ranges.append(int(line.split()[2]))

    return GardenMap(sources, destinations, ranges)


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

seed2soil: GardenMap = parse_to_class(lines[index_list[0][0]:index_list[0][1]])
soil2fert: GardenMap = parse_to_class(lines[index_list[1][0]:index_list[1][1]])
fert2water: GardenMap = parse_to_class(lines[index_list[2][0]:index_list[2][1]])
water2light: GardenMap = parse_to_class(lines[index_list[3][0]:index_list[3][1]])
light2temp: GardenMap = parse_to_class(lines[index_list[4][0]:index_list[4][1]])
temp2hum: GardenMap = parse_to_class(lines[index_list[5][0]:index_list[5][1]])
hum2loc: GardenMap = parse_to_class(lines[index_list[6][0]:index_list[6][1]])

map_list: list[GardenMap] = [seed2soil, soil2fert, fert2water, water2light, light2temp, temp2hum, hum2loc]

locations: list[int] = []
for seed in seeds:
    input: int = seed
    for maps in map_list:
        input = maps.get_output_from_input(input)

    locations.append(input)

print(f'Day 5 - Part 1: {min(locations)}')

input_ranges: list[list[int]] = [hum2loc.get_min_output_inputs()]
min_loc = max(locations)

map_list.reverse()

for maps in map_list[1:]:
    input_ranges = maps.get_input_ranges_from_output_ranges(input_ranges)


valid_input_seeds = list(input_ranges)

map_list.reverse()

for seed_range in batched(seeds, 2):
    for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
        if seed == 82:
            pass
        if seed not in valid_input_seeds:
            continue
        
        input: int = seed        
        for maps in map_list:
            input = maps.get_output_from_input(input)

        min_loc = min(min_loc, input)
        

print(min_loc)
# print(min(hum2loc.output_start))