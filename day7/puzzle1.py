import requests
from collections import Counter


def get_puzzle_input(url):
    cookies = dict(session='3616c7465645f5f13b7afa779027751d5fe355ad05134f32f314ec950f4ed097a749be6824c7418863e171bbcb42695785bc3e21b479ad827050985fbd210b6')
    r = requests.get(url, cookies = cookies)
    return r.text


def get_puzzle_test_input():
    input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
    output = 6440
    return input, output

def test_puzzle(input, expect_result):
    actual_result = solve_puzzle(input)
    print('')
    if actual_result == expect_result:
        print('Well done!', actual_result, '==', expect_result)
    else:
        print('You got an error', actual_result, '<>', expect_result)
    print('')


def solve_puzzle(input: str):
    combination_list = [ 'five', 'four', 'full_house', 'three', 'two_pair', 'one_pair', 'high_card' ]
    combinations = { comb:[] for comb in combination_list }

    # define the mapping table
    mapping_table = str.maketrans({
        'A': 'a', 'K': 'b', 'Q': 'c', 'J': 'd', 'T': 'e', '9': 'f',
        '8': 'g', '7': 'h', '6': 'i', '5': 'j', '4': 'k', '3': 'l', '2': 'm' 
    })

    hands = {}
    hand_map = {}
    for line in input.splitlines():
    # for origin_hand, bid in hands.items():
        
        origin_hand, bid = line.split(' ')
        hands[origin_hand] = int(bid)

        hand = origin_hand.translate(mapping_table)
        hand_map[hand] = origin_hand

        group = Counter(list(hand))
        # five
        if len(group) == 1:
            combinations['five'].append(hand)
        # four or full house
        if len(group) == 2:
            max_key = max(group, key=group.get)
            if group[max_key] == 4:
                combinations['four'].append(hand)
            elif group[max_key] == 3:
                combinations['full_house'].append(hand)
        # tree or two pair
        if len(group) == 3:
            max_key = max(group, key=group.get)
            if group[max_key] == 3:
                combinations['three'].append(hand)
            else:
                combinations['two_pair'].append(hand)
        # one pair
        if len(group) == 4:
            combinations['one_pair'].append(hand)
        # high card
        if len(group) == 5:
            combinations['high_card'].append(hand)


    rank_list = []
    combination_list.reverse()
    for comb in combination_list:
        if len(combinations[comb]) > 0:
            rank_list += sorted(combinations[comb], reverse=True)

    total = 0
    for i, hand in enumerate(rank_list):
        total += (i + 1) * hands[hand_map[hand]]

    return total


if __name__ == '__main__':
    # test
    input, output = get_puzzle_test_input()
    test_puzzle(input, output)

    # exit()

    # real example
    input = get_puzzle_input('https://adventofcode.com/2023/day/7/input')
    output = solve_puzzle(input)
    print('')
    print("The answer is", output)
    print('')
