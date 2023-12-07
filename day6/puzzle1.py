import requests
from collections import defaultdict
import re


def get_puzzle_input(url):
    cookies = dict(session='3616c7465645f5f13b7afa779027751d5fe355ad05134f32f314ec950f4ed097a749be6824c7418863e171bbcb42695785bc3e21b479ad827050985fbd210b6')
    r = requests.get(url, cookies = cookies)
    return r.text


def get_puzzle_test_input():
    input = """Time:      7  15   30
Distance:  9  40  200
"""
    output = 288
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

    times = [int(x) for x in re.split(r'\W+', time_line.strip())]
    _, distance_line = lines[1].split(':')
    distances = [int(x) for x in re.split(r'\W+', distance_line.strip())]

    races = {}
    for i, max_time in enumerate(times):
        ways = {}
        time = 1
        while time <= max_time:
            hold_time = speed =  time
            ways[time] = {
                'hold_time': hold_time,
                'speed': speed,
                'distance': speed * (max_time - hold_time)
            }
            time += 1
        races[i] = ways
        
    suit_ways = defaultdict(list)
    for i, distance in enumerate(distances):
        for time, way in races[i].items():
            if way['distance'] > distance:
                suit_ways[i].append(time)

    result = 1
    for _, suit_way in suit_ways.items():
        result *= len(suit_way)

    return result


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
