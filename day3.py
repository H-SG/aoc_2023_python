from utils import read_to_array
import re

lines = read_to_array('data/day3.txt')
max_lines: int = len(lines)

valid_digits: list[int] = []
gear_ratio_sum = 0

digit_finder = r'(\d+)'
symbols_finder = r'[^\d|\.]'

for line_index, line in enumerate(lines):
    search_lines = []

    if line_index > 0:
        search_lines.append(line_index - 1)
    search_lines.append(line_index)
    if line_index < max_lines - 1:
        search_lines.append(line_index + 1)

    line_digits: list[str] = set(re.findall(digit_finder, line))
    
    for line_digit in line_digits:
        sub_indices: list[int] = [[match.start(), match.end()] for match in re.finditer(fr'(\D|^)(\b){line_digit}(\b)(\D|$)', line)]

        for sub_index in sub_indices:
            for search_line in search_lines:
                if re.findall(symbols_finder, lines[search_line][sub_index[0]:sub_index[1]]):
                    valid_digits.append(int(line_digit))
                    break

    gear_indices: list[int] = [match.start() for match in re.finditer(f'\*', line)]
    
    for gear_index in gear_indices:
        match_digits = []

        for search_line in search_lines:
            line_digits: list[str] = set(re.findall(digit_finder, lines[search_line]))
            
            for line_digit in line_digits:
                matches = [[x for x in range(match.start(), match.end())] for match in re.finditer(fr'(\D|^)(\b){line_digit}(\b)(\D|$)', lines[search_line])]
    
                for match in matches:
                    if gear_index in match:
                        match_digits.append(int(line_digit))

        if len(match_digits) == 2:
            gear_ratio_sum += match_digits[0] * match_digits[1]

print(f'Day 3 - Part 1: {sum(valid_digits)}')
print(f'Day 3 - Part 2: {gear_ratio_sum}')
