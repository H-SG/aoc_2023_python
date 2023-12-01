from utils import read_to_array

lines = read_to_array('data/day1.txt')

def line_to_int(line: str) -> int:
    if len(line) > 2:
        line = f'{line[0]}{line[-1]}'

    if len(line) == 1:
        line = f'{line[0]}{line[0]}'

    if len(line) == 0:
        line = 0

    return int(line)

# part 1
part_1_lines = []
for i in range(len(lines)):
    part_1_lines.append(lines[i])
    for char in range(97, 97+26):
        part_1_lines[-1] = part_1_lines[-1].replace(chr(char), "")

    part_1_lines[-1] = line_to_int(part_1_lines[-1])

print(f'Day 1 - Part 1: {sum(part_1_lines)}')

# part 2
word_values = {'one':'1',
               'two':'2',
               'three':'3',
               'four':'4',
               'five':'5',
               'six':'6',
               'seven':'7',
               'eight':'8',
               'nine':'9'}

part_2_lines = []
for i in range(len(lines)):
    part_2_lines.append('')
    j = 0
    while j < len(lines[i]):
        if lines[i][j].isdigit():
            part_2_lines[-1] += lines[i][j]
            j += 1
            continue

        for word, value in word_values.items():
            try:
                if lines[i][j:j + len(word)] == word:
                    part_2_lines[-1] += value

                    # there can be overlap between the end of one word digit and the start of another word digit
                    j += len(word) - 1
                    break
                else:
                    continue
            except IndexError:
                continue
        else:
            j += 1

    part_2_lines[i] = line_to_int(part_2_lines[i])

print(f'Day 1 - Part 2: {sum(part_2_lines)}')
