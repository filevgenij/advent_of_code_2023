import requests
from collections import defaultdict


def get_puzzle_input(url):
    cookies = dict(session='3616c7465645f5f13b7afa779027751d5fe355ad05134f32f314ec950f4ed097a749be6824c7418863e171bbcb42695785bc3e21b479ad827050985fbd210b6')
    r = requests.get(url, cookies = cookies)
    return r.text


def get_puzzle_test_input():
    input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
    output = 4361
    return input, output

def test_puzzle(input, expect_result):
    actual_result = solve_puzzle(input)
    print('')
    if actual_result == expect_result:
        print('Well done!', actual_result, '==', expect_result)
    else:
        print('You got an error', actual_result, '<>', expect_result)
    print('')


def check_adjacent_symbol(lines, number_position, number_seq):
    last_line_index = len(lines) - 1
    last_col_index = len(lines[0]) - 1

    # there is line above, check it
    top_row_index = number_position['line_number'] - 1 if number_position['line_number'] != 0 else number_position['line_number']

    # there is line belowe, check it
    bottom_row_index = number_position['line_number'] + 1 if number_position['line_number'] != last_line_index else number_position['line_number']

    # there is column behid, check it
    top_col_index = number_position['position_in_line'] - 1 if number_position['position_in_line'] !=0 else number_position['position_in_line']
    
    #there is column ahead, check it
    bottom_col_index = number_position['position_in_line'] + len(number_seq) + 1 if number_position['position_in_line'] + len(number_seq) < last_col_index else number_position['position_in_line'] + len(number_seq)

    for r_index in range(top_row_index, bottom_row_index + 1):
        for c_index in range(top_col_index, bottom_col_index):
            symbol = lines[r_index][c_index]
            if not symbol.isnumeric() and symbol != '.':
                return True

    return False


def solve_puzzle(input: str):
    lines = input.splitlines()
    number_sec = []
    number_position = { 'line_number': 0, 'position_in_line':0 }
    sum_of_numbers = 0
    for line_number, line in enumerate(lines):
        for i, chr in enumerate(line):
            if chr.isnumeric():
                if len(number_sec) == 0:
                    # find new number, fix it position
                    number_position = {'line_number': line_number, 'position_in_line': i}
                number_sec.append(chr)
            else:
                if len(number_sec) > 0:
                    #check adjacent symbol 
                    if check_adjacent_symbol(lines, number_position, number_sec):
                        # if so add the number to sum
                        sum_of_numbers += int(''.join(number_sec))
                    # clean up stored number sequence
                    number_sec = []
        # end of line, need to check
        if len(number_sec) > 0:
            #check adjacent symbol 
            if check_adjacent_symbol(lines, number_position, number_sec):
                # if so add the number to sum
                sum_of_numbers += int(''.join(number_sec))
            # clean up stored number sequence
            number_sec = []

    return sum_of_numbers

if __name__ == '__main__':
    # test
    input, output = get_puzzle_test_input()
    test_puzzle(input, output)

    # exit()

    # real example
    input = get_puzzle_input('https://adventofcode.com/2023/day/3/input')
    output = solve_puzzle(input)
    print('')
    print("The answer is", output)
    print('')
