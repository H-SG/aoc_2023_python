from __future__ import annotations
from utils import read_to_array
from dataclasses import dataclass
from copy import deepcopy
from itertools import combinations

lines: list[str] = read_to_array('data/day7.txt')

@dataclass
class Hand():
    cards: list[str]
    bet: int
    type: int = 0
    rank: int = 0
    ranked: bool = False
    losses: int = 0

    def __post_init__(self) -> None:
        self.original_cards = deepcopy(self.cards)
        self.type = self.get_type(self.cards)
        self.card_strength: list[int] =  self.get_hand_strength(self.cards)   

    def get_alt_score_hand(self) -> Hand:
        new_hand = deepcopy(self)

        unique_cards: list[str] = list(set(new_hand.cards))
        unique_cards_counts: list[int] = [new_hand.cards.count(x) for x in unique_cards]

        for i, s in enumerate(new_hand.card_strength):
            if s == 11:
                new_hand.card_strength[i] = 1

        valid_unique_cards: list[int] = []
        valid_unique_cards_counts: list[int] = []
        for c, n in zip(unique_cards, unique_cards_counts):
            if c == 'J':
                continue

            valid_unique_cards.append(c)
            valid_unique_cards_counts.append(n)

        if len(valid_unique_cards_counts):
            max_cards = max(valid_unique_cards_counts)
        else:
            max_cards = 0

        strongest_card_score: int = 1
        for c, n in zip(valid_unique_cards, valid_unique_cards_counts):
            if n == max_cards:
                strongest_card_score = max(strongest_card_score, self.get_card_strength(c))
        
        match strongest_card_score:
            case 14:
                strongest_card = 'A'
            case 13:
                strongest_card = 'K'
            case 12:
                strongest_card = 'Q'
            case 10:
                strongest_card = 'T'
            case 1:
                strongest_card = 'J'
            case val:
                strongest_card = str(val)

        if 'J' in new_hand.cards:
            for i, card in enumerate(new_hand.cards):
                if card == 'J':
                    new_hand.cards[i] = strongest_card

        new_hand.type = self.get_type(new_hand.cards)

        return new_hand

    def get_type(self, cards: list[str]) -> int:
        unique_cards: list[str] = list(set(cards))
        n_unique_cards: int = len(unique_cards)
        card_counts: list[int] = [cards.count(x) for x in unique_cards]

        match n_unique_cards:
            case 5:
                return 0
            case 4:
                return 1
            case 3:
                if 3 in card_counts:
                    return 3
                else:
                    return 2
            case 2:
                if 3 in card_counts:
                    return 4
                else:
                    return 5
            case 1:
                return 6
            
        raise ValueError()

    def get_hand_strength(self, cards: list[str]) -> list[int]:
        card_strength: list[int] = []

        for card in cards:
            card_strength.append(self.get_card_strength(card))

        return card_strength
    
    def get_card_strength(self, card: str, alt_score: bool = False) -> int:
        match card:
                case 'A':
                    return 14
                case 'K':
                    return 13
                case 'Q':
                    return 12
                case 'J':
                    if alt_score:
                        return 1
                    else:
                        return 11
                case 'T':
                    return 10
                case val:
                    return int(val)

    def check_win(self, hand: Hand) -> bool:
        for c, h in zip(self.card_strength, hand.card_strength):
            if c == h:
                continue

            if c > h:
                hand.losses += 1
                return True
            
            if c < h:
                self.losses += 1
                return False
            

hand_dict: dict = {}
alt_hand_dict = {}

for line in lines:
    current_hand: Hand = Hand([x for x in line.split()[0]], int( line.split()[1]))
    alt_hand = current_hand.get_alt_score_hand()

    if current_hand.type in hand_dict.keys():
        hand_dict[current_hand.type].append(current_hand)
    else:
        hand_dict[current_hand.type] = [current_hand]

    if alt_hand.type in alt_hand_dict.keys():
        alt_hand_dict[alt_hand.type].append(alt_hand)
    else:
        alt_hand_dict[alt_hand.type] = [alt_hand]

hand_dict = dict(sorted(hand_dict.items()))
alt_hand_dict = dict(sorted(alt_hand_dict.items()))

def get_winnings(hands_dict: dict) -> int:
    total_winnings: int = 0
    current_rank: int = 1
    
    for type, hands in hands_dict.items():
        n_hands: int = len(hands)
        max_hands_score: int = current_rank + n_hands - 1

        for card1, card2 in combinations(hands, 2):
            card1.check_win(card2)

        for hand in hands:
            hand.rank = max_hands_score - hand.losses
            total_winnings += hand.rank * hand.bet

        current_rank = max_hands_score + 1
        
    return total_winnings

print(f'Day 7 - Part 1: {get_winnings(hand_dict)}')
print(f'Day 7 - Part 2: {get_winnings(alt_hand_dict)}')