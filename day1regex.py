import re
from utils import read_to_array

def word_to_int(word: str) -> int:
    match word:
        case 'one'|'1':
            return 1
        case 'two'|'2':
            return 2
        case 'three'|'3':
            return 3
        case 'four'|'4':
            return 4
        case 'five'|'5':
            return 5
        case 'six'|'6':
            return 6
        case 'seven'|'7':
            return 7
        case 'eight'|'8':
            return 8
        case 'nine'|'9':
            return 9
        case _:
            raise ValueError()

lines = read_to_array('data/day1.txt')
pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))'
sum = 0

for line in lines:
    digits = re.findall(pattern, line)
    sum += int(f'{word_to_int(digits[0])}{word_to_int(digits[-1])}')
        
print(sum)