import requests


def get_puzzle_input(url):
    cookies = dict(session='3616c7465645f5f13b7afa779027751d5fe355ad05134f32f314ec950f4ed097a749be6824c7418863e171bbcb42695785bc3e21b479ad827050985fbd210b6')
    r = requests.get(url, cookies = cookies)
    return r.text


def get_puzzle_test_input():
    input = """Time:      7  15   30
Distance:  9  40  200
"""
    output = 71503
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
    _, time_line = lines[0].split(':')
    _, distance_line = lines[1].split(':')

    max_time = int(time_line.replace(' ', ''))
    distance_race = int(distance_line.replace(' ', ''))

    # find min suitable time
    time = 1
    while True:
        hold_time = speed =  time
        if distance_race < speed * (max_time - hold_time):
            break
        time += 1

    time_start = time

    # find max suitable time
    time = max_time
    while True:
        hold_time = speed =  time
        if distance_race < speed * (max_time - hold_time):
            break
        time -= 1

    time_end = time

    return time_end - time_start + 1


if __name__ == '__main__':
    # test
    input, output = get_puzzle_test_input()
    test_puzzle(input, output)

    # exit()

    # real example
    input = get_puzzle_input('https://adventofcode.com/2023/day/6/input')
    output = solve_puzzle(input)
    print('')
    print("The answer is", output)
    print('')
