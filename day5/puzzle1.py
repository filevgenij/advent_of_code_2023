import requests
from collections import defaultdict


def get_puzzle_input(url):
    cookies = dict(session='3616c7465645f5f13b7afa779027751d5fe355ad05134f32f314ec950f4ed097a749be6824c7418863e171bbcb42695785bc3e21b479ad827050985fbd210b6')
    r = requests.get(url, cookies = cookies)
    return r.text


def get_puzzle_test_input():
    input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
    output = 35
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
    is_seed_to_soil_map = False
    is_soil_to_fertilizer_map = False
    is_fertilizer_to_water_map = False
    is_water_to_light_map = False
    is_light_to_temperature_map = False
    is_temperature_to_humidity_map = False
    is_humidity_to_location_map = False
    rules = defaultdict(list)
    for line in lines:
        if line == '':
            continue
        if line.startswith('seeds'):
            _, seeds_numbers_line = line.split(':')
            continue
        if line.startswith('seed-to-soil map'):
            is_seed_to_soil_map = True
            continue
        if line.startswith('soil-to-fertilizer map'):
            is_seed_to_soil_map = False
            is_soil_to_fertilizer_map = True
            continue
        if line.startswith('fertilizer-to-water map'):
            is_soil_to_fertilizer_map = False
            is_fertilizer_to_water_map = True
            continue
        if line.startswith('water-to-light map'):
            is_fertilizer_to_water_map = False
            is_water_to_light_map = True
            continue
        if line.startswith('light-to-temperature map'):
            is_water_to_light_map = False
            is_light_to_temperature_map = True
            continue
        if line.startswith('temperature-to-humidity map'):
            is_light_to_temperature_map = False
            is_temperature_to_humidity_map = True
            continue
        if line.startswith('humidity-to-location map'):
            is_temperature_to_humidity_map = False
            is_humidity_to_location_map = True
            continue
        
        if is_seed_to_soil_map:
            rules['seed_to_soil_map'].append([int(x) for x in line.split(' ')])
        if is_soil_to_fertilizer_map:
            rules['soil_to_fertilizer_map'].append([int(x) for x in line.split(' ')])
        if is_fertilizer_to_water_map:
            rules['fertilizer_to_water_map'].append([int(x) for x in line.split(' ')])
        if is_water_to_light_map:
            rules['water_to_light_map'].append([int(x) for x in line.split(' ')])
        if is_light_to_temperature_map:
            rules['light_to_temperature_map'].append([int(x) for x in line.split(' ')])
        if is_temperature_to_humidity_map:
            rules['temperature_to_humidity_map'].append([int(x) for x in line.split(' ')])
        if is_humidity_to_location_map:
            rules['humidity_to_location_map'].append([int(x) for x in line.split(' ')])

        locations = []
        for seed in seeds_numbers_line.strip().split(' '):
            soil = get_mapped_value(int(seed), rules['seed_to_soil_map'])
            fertilizerer = get_mapped_value(soil, rules['soil_to_fertilizer_map'])
            water = get_mapped_value(fertilizerer, rules['fertilizer_to_water_map'])
            light = get_mapped_value(water, rules['water_to_light_map'])
            temperature = get_mapped_value(light, rules['light_to_temperature_map'])
            humidity = get_mapped_value(temperature, rules['temperature_to_humidity_map'])
            location = get_mapped_value(humidity, rules['humidity_to_location_map'])

            locations.append(location)

    return min(locations)


def get_mapped_value(input, map):
    for rule in map:
        dest, source, length = rule
        if input >= source and input < source + length:
            return dest + (input - source)

    return input


if __name__ == '__main__':
    # test
    input, output = get_puzzle_test_input()
    test_puzzle(input, output)

    # exit()

    # real example
    input = get_puzzle_input('https://adventofcode.com/2023/day/5/input')
    output = solve_puzzle(input)
    print('')
    print("The answer is", output)
    print('')
