import requests


def get_puzzle_input(url):
    cookies = dict(session='3616c7465645f5f13b7afa779027751d5fe355ad05134f32f314ec950f4ed097a749be6824c7418863e171bbcb42695785bc3e21b479ad827050985fbd210b6')
    r = requests.get(url, cookies = cookies)
    return r.text


def get_puzzle_test_input():
    input = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""
    output = 4
    # a little bit complicated input 
    input = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""
    output = 8
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
    pipe_map = []
    S = {}
    for r, line in enumerate(input.splitlines()):
        pipe_map.append(list(line))
        if 'S' in line:
            S = {'r': r, 'c': line.find('S')}

    rules = {
        '|': {'1_0': {'r': -1, 'c' : 0}, '-1_0': {'r': 1, 'c': 0}}, # is a vertical pipe connecting north and south.
        '-': {'0_-1': {'r': 0, 'c': 1}, '0_1': {'r':0, 'c': -1}}, #is a horizontal pipe connecting east and west.
        'L': {'0_1': {'r': -1, 'c': 0}, '-1_0': {'r': 0, 'c': 1}}, # is a 90-degree bend connecting north and east.
        'J': {'-1_0': {'r': 0, 'c': -1}, '0_-1': {'r': -1, 'c': 0}}, # is a 90-degree bend connecting north and west 
        '7': {'0_-1': {'r':1, 'c': 0}, '1_0': {'r': 0, 'c': -1}}, # is a 90-degree bend connecting south and west.
        'F': {'1_0': {'r': 0, 'c': 1}, '0_1': {'r': 1, 'c': 0}}, # is a 90-degree bend connecting south and east
    }

    # determinate S
    top = pipe_map[S['r']-1][S['c']]
    bottom = pipe_map[S['r']+1][S['c']]
    left = pipe_map[S['r']][S['c']-1]
    right = pipe_map[S['r']][S['c']+1]
    c_pipe = ''
    if top in ('7', '|', 'F') and bottom in ('L', '|', 'J'):
        c_pipe = '|'
        pr = S['r']-1
        pc = S['c']
    elif left in ('F', '-', 'L') and right in ('J', '-', '7'):
        c_pipe = '-'
        pr = S['r']
        pc = S['c']-1
    elif top in ('7', '|', 'F') and right in ('J', '-', '7'):
        c_pipe = 'L'
        pr = S['r']-1
        pc = S['c']
    elif top in ('7', '|', 'F') and left in ('F', '-', 'L'):
        c_pipe = 'J'
        pr = S['r']-1
        pc = S['c']
    elif bottom in ('L', '|', 'J') and left in ('F', '-', 'L'):
        c_pipe = '7'
        pr = S['r']+1
        pc = S['c']
    elif bottom in ('L', '|', 'J') and right in ('J', '-', '7'):
        c_pipe = 'F'
        pr = S['r']+1
        pc = S['c']

    cr = S['r']
    cc = S['c']
    steps = 0
    while True:
        dr = pr - cr
        dc = pc - cc
        key = '{}_{}'.format(dr, dc)
        nr = cr + rules[c_pipe][key]['r']
        nc = cc + rules[c_pipe][key]['c']
        steps += 1
        # check to back at the begining
        if  nr == S['r'] and nc == S['c']:
            break
        c_pipe = pipe_map[nr][nc]
        pr = cr
        pc = cc
        cr = nr
        cc = nc

    return int(steps / 2)


if __name__ == '__main__':
    # test
    input, output = get_puzzle_test_input()
    test_puzzle(input, output)

    # exit()

    # real example
    input = get_puzzle_input('https://adventofcode.com/2023/day/10/input')
    output = solve_puzzle(input)
    print('')
    print("The answer is", output)
    print('')
