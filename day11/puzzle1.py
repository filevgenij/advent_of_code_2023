import requests
import math


def get_puzzle_input(url):
    cookies = dict(session='3616c7465645f5f13b7afa779027751d5fe355ad05134f32f314ec950f4ed097a749be6824c7418863e171bbcb42695785bc3e21b479ad827050985fbd210b6')
    r = requests.get(url, cookies = cookies)
    return r.text


def get_puzzle_test_input():
    input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""
    output = 374
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
    image = []
    empty_row = []
    empty_col = []

    for r, line in enumerate(input.splitlines()):
        # find empty rows
        if '#' not in line:
            empty_row.append(r)
        image.append(list(line))

    # find empty cols
    for c in range(0, len(image[0])):
        is_empty_col = True
        for r in range(0, len(image)):
            if image[r][c] == '#':
                is_empty_col = False
                break
        if is_empty_col:
            empty_col.append(c)

    # expand columns
    empty_col.reverse()
    for c in empty_col:
        for r in range(0, len(image)):
            image[r].insert(c, '.')
    
    #expand rows
    empty_row.reverse()
    for r in empty_row:
        image.insert(r, image[r])
    
    galaxies = []
    # find all pair
    for r, row in enumerate(image):
        for c, cell in enumerate(row):
            if cell == '#':
                galaxies.append('{}_{}'.format(r, c))

    i = 0
    # make a pairs
    pairs = []
    while i < len(galaxies) - 1:
        first = galaxies[i]
        for elem in galaxies[i+1::]:
            pairs.append((first, elem))
        i += 1

    sum_of_lenght = 0
    #find closer distance
    for pair in pairs:
        sum_of_lenght += len(get_closer_distance(*pair, len(image), len(image[0])))

    return sum_of_lenght


def get_closer_distance(first, last, max_r, max_c):
    fr, fc = [int(x) for x in first.split('_')]
    lr, lc = [int(x) for x in last.split('_')]

    cr, cc = fr, fc
    path = []
    while True:
        next_steps = []
        if cr != 0:
            next_steps.append((cr-1, cc))
        if cr != max_r:
            next_steps.append((cr+1, cc))
        if cc != 0:
            next_steps.append((cr, cc-1))
        if cc != max_c:
            next_steps.append((cr, cc+1))

        distances = {}
        for next_step in next_steps:
            distances[next_step] = math.sqrt((next_step[0]-lr)**2 + (next_step[1]-lc)**2)

        nr, nc = min(distances, key=distances.get)
        path.append('{}_{}'.format(nr, nc))
        cr, cc = nr, nc
        if lr == nr and lc == nc:
            break

    return path

if __name__ == '__main__':
    # test
    input, output = get_puzzle_test_input()
    test_puzzle(input, output)

    # exit()

    # real example
    input = get_puzzle_input('https://adventofcode.com/2023/day/11/input')
    output = solve_puzzle(input)
    print('')
    print("The answer is", output)
    print('')
