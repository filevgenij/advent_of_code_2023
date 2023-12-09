import requests
from collections import Counter
from itertools import cycle


def get_puzzle_input(url):
    cookies = dict(session='3616c7465645f5f13b7afa779027751d5fe355ad05134f32f314ec950f4ed097a749be6824c7418863e171bbcb42695785bc3e21b479ad827050985fbd210b6')
    r = requests.get(url, cookies = cookies)
    return r.text


def get_puzzle_test_input():
    input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""
    output = 114
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
    total = 0
    differences = {}
    for num, line in enumerate(input.splitlines()):
        differences[num] = [[int(x) for x in line.split(' ')]]
        k = 0
        while True:
            i = 1
            diff = []
            zero_cnt = 0
            last_history = differences[num][k]
            while i < len(last_history):
                diff_value = last_history[i] - last_history[i - 1]
                if diff_value == 0:
                    zero_cnt += 1
                diff.append(diff_value)
                i += 1
            differences[num].append(diff)
            k += 1
            if len(diff) == zero_cnt:
                break

        # add zero to last diff
        differences[num][k].append(0)
        # move k to next line up
        k -= 1
        while k >= 0:
            differences[num][k].append(differences[num][k+1][-1] + differences[num][k][-1])
            k -= 1
        total += differences[num][0][-1]

    return total


if __name__ == '__main__':
    # test
    input, output = get_puzzle_test_input()
    test_puzzle(input, output)

    # exit()

    # real example
    input = get_puzzle_input('https://adventofcode.com/2023/day/9/input')
    output = solve_puzzle(input)
    print('')
    print("The answer is", output)
    print('')
