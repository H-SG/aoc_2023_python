from utils import read_to_array
import re

lines = read_to_array('data/day3.txt')
max_lines: int = len(lines)
max_line_length: int = len(lines[0])

valid_digits: list[int] = []

digit_finder = r'(\d+)'
symbols_finder = r'[^\d|\.]'

for line_index, line in enumerate(lines):
    line_digits: list[str] = set(re.findall(digit_finder, line))

    if len(line_digits) == 0:
        continue
    
    for line_digit in line_digits:
        digit_length: int = len(line_digit)
        sub_indices: list[int] = [match.start() for match in re.finditer(line_digit, line)]
        search_lines = [max(0, line_index - 1), line_index, min(max_lines - 1, line_index + 1)]
        

        for sub_index in sub_indices:
            
            if sub_index != 0:
                if line[sub_index - 1].isdigit():
                    continue

            end_index = sub_index + len(line_digit)
            if end_index < max_line_length:
                if line[end_index].isdigit():
                    continue

            line_search_range = [max(0, sub_index - 1), min(max_line_length, sub_index + digit_length + 1)]

            adjacent_chars = ''
            for search_line in search_lines:
                adjacent_chars += lines[search_line][line_search_range[0]:line_search_range[1]]

            symbols = re.findall(symbols_finder, adjacent_chars)

            if len(symbols) > 0:
                valid_digits.append(int(line_digit))


gear_ratio_sum = 0

for line_index, line in enumerate(lines):
    if '*' not in line:
        continue

    sub_indices: list[int] = [match.start() for match in re.finditer(f'\*', line)]
    search_lines = []

    if line_index > 0:
        search_lines.append(line_index - 1)

    search_lines.append(line_index)

    if line_index < max_lines - 1:
        search_lines.append(line_index + 1)

    if line_index == 107:
        pass

    
    for sub_index in sub_indices:
        match_digits = []
        for search_line in search_lines:
            line_digits: list[str] = set(re.findall(digit_finder, lines[search_line]))
            for line_digit in line_digits:
                matches = [[x for x in range(match.start() - 1, match.end() + 1)] for match in re.finditer(line_digit, lines[search_line])]
                if line_digit == 447:
                    pass
                for match in matches:
                    if lines[search_line][match[0]].isdigit():
                        continue

                    try:
                        if lines[search_line][match[-1]].isdigit():
                            continue
                    except:
                        pass

                    if sub_index in match:
                        match_digits.append(int(line_digit))

        if len(match_digits) == 2:
            gear_ratio_sum += match_digits[0] * match_digits[1]


print(sum(valid_digits))
print(gear_ratio_sum)