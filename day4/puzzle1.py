import requests
from collections import defaultdict


def get_puzzle_input(url):
    cookies = dict(session='3616c7465645f5f13b7afa779027751d5fe355ad05134f32f314ec950f4ed097a749be6824c7418863e171bbcb42695785bc3e21b479ad827050985fbd210b6')
    r = requests.get(url, cookies = cookies)
    return r.text


def get_puzzle_test_input():
    input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
    output = 13
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
    lines = input.splitlines()
    total_points = 0
    for line in lines:
        cards, numbers = line.split(':')
        # _, card_number = cards.split(' ')
        win_numbers_line, my_numbers_line = numbers.split('|')
        win_numbers = win_numbers_line.strip().replace('  ', ' ').split(' ')
        my_numbers = my_numbers_line.strip().replace('  ', ' ').split(' ')
        card_point = 0
        for win_number in win_numbers:
            if win_number in my_numbers:
                if card_point == 0:
                    card_point = 1
                else:
                    card_point *= 2
        total_points += card_point

    return total_points


if __name__ == '__main__':
    # test
    input, output = get_puzzle_test_input()
    test_puzzle(input, output)

    # exit()

    # real example
    input = get_puzzle_input('https://adventofcode.com/2023/day/4/input')
    output = solve_puzzle(input)
    print('')
    print("The answer is", output)
    print('')
