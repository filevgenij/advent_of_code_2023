import requests
from itertools import cycle


def get_puzzle_input(url):
    cookies = dict(session='3616c7465645f5f13b7afa779027751d5fe355ad05134f32f314ec950f4ed097a749be6824c7418863e171bbcb42695785bc3e21b479ad827050985fbd210b6')
    r = requests.get(url, cookies = cookies)
    return r.text


def get_puzzle_test_input():
    input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""
    output = 6
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

    node_map = {}
    for i, line in enumerate(lines):
        if i == 0:
            instructions = [*line]
            continue
        if line == '':
            continue
        node_key, node_instructions = line.split('=')
        left_instr, right_instr = node_instructions.strip().strip('(').strip(')').split(',')
        node_map[node_key.strip()] = {
            'L': left_instr.strip(),
            'R': right_instr.strip()
        }

    node = 'AAA'
    end_node = 'ZZZ'
    steps = 0
    for instr in cycle(instructions):
        steps += 1
        next_node = node_map[node][instr]
        if next_node != end_node:
            node = next_node
        else:
            break

    return steps 


if __name__ == '__main__':
    # test
    input, output = get_puzzle_test_input()
    test_puzzle(input, output)

    # exit()

    # real example
    input = get_puzzle_input('https://adventofcode.com/2023/day/8/input')
    output = solve_puzzle(input)
    print('')
    print("The answer is", output)
    print('')
