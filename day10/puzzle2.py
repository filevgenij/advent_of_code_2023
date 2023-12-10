import requests


def get_puzzle_input(url):
    cookies = dict(session='3616c7465645f5f13b7afa779027751d5fe355ad05134f32f314ec950f4ed097a749be6824c7418863e171bbcb42695785bc3e21b479ad827050985fbd210b6')
    r = requests.get(url, cookies = cookies)
    return r.text


def get_puzzle_test_input():
    input = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""
    output = 10
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
    path = {'{}_{}'.format(cr, cc): c_pipe}
    pipe_map[cr][cc] = c_pipe
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
        path['{}_{}'.format(cr, cc)] = c_pipe

    total = 0
    pipe_map[cr][cc] = c_pipe
    for r, row in enumerate(pipe_map):
        matrix_row = []
        save_elements = ''
        crossing_vertical = 0
        for c, elem in enumerate(row):
            key = '{}_{}'.format(r, c)
            if key in path:
                if elem == '|':
                    crossing_vertical += 1
                elif elem != '-':
                    if len(save_elements) < 2:
                        save_elements += elem
                    if len(save_elements) == 2:
                        if save_elements in ['FJ', 'L7']:
                            crossing_vertical += 1
                        save_elements = ''
                matrix_row.append(elem)
            else:
                matrix_row.append(crossing_vertical)
        total += sum([1 for x in matrix_row if type(x) == int and x%2])

    return total


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
