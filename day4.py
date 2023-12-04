from utils import read_to_array
from dataclasses import dataclass
import datetime as dt

start: dt.datetime = dt.datetime.now()

@dataclass
class Card():
    card_id: int
    win_num: list[int]
    card_num: list[int]
    matches: int = 0
    score_1: int = 0

    def __post_init__(self) -> None:
        for num in self.win_num:
            if num in self.card_num:
                if self.score_1 == 0:
                    self.score_1 = 1
                else:
                    self.score_1 *= 2

                self.matches += 1

card_dict: dict = {}

lines: list[str] = read_to_array('data/day4.txt')
total_score: int = 0
for line in lines:
    card_id: int = int(line.split(':')[0].strip().split(' ')[-1])

    if card_id in card_dict.keys():
        card_dict[card_id] += 1
    else:
        card_dict[card_id] = 1

    win_num: str = line.split(':')[-1].strip().split('|')[0].strip()
    card_num: str = line.split(':')[-1].strip().split('|')[-1].strip()

    current_card: Card = Card(
        card_id, 
        [int(x) for x in win_num.split()],
        [int(x) for x in card_num.split()]
    )
    
    total_score += current_card.score_1

    for i in range(card_id + 1, card_id + current_card.matches + 1):
        if i in card_dict.keys():
            card_dict[i] += card_dict[card_id]
        else:
            card_dict[i] = card_dict[card_id]

print(f'Day 4 - Part 1: {total_score}')
print(f'Day 4 - Part 2: {sum(card_dict.values())}')
print(f'Loading and both solutions took {(dt.datetime.now() - start).total_seconds()} seconds')
