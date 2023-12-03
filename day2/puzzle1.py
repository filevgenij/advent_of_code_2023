import requests

def get_puzzle_input(url):
    cookies = dict(session='3616c7465645f5f13b7afa779027751d5fe355ad05134f32f314ec950f4ed097a749be6824c7418863e171bbcb42695785bc3e21b479ad827050985fbd210b6')
    r = requests.get(url, cookies = cookies)
    return r.text

def get_puzzle_test_input():
    input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
    output = 8
    return input, output

def test_puzzle(input, expect_result):
    actual_result = solve_puzzle(input)
    try:
        print('')
        assert actual_result == expect_result
    except AssertionError:
        print('You got an error', actual_result, '<>', expect_result)
    else:
        print('Well done!', actual_result, '==', expect_result)
    
    print('')

def parse_input(input: str):
    """
    Return {game_id: {combination_id:{red:0, green:0, blue:0}}}
    for instanse {1: {0: {'red':0, 'green':0, 'blue':0}, 1:{'red':0,'green':0, 'blue':0}}}
    """
    lines = input.splitlines()
    games = {}
    for line in lines:
        game, combinations_line = line.split(':')
        _, game_number = game.split(' ')
        game_number = int(game_number)
        combinations = combinations_line.split(';')
        for i, combination in enumerate(combinations):
            cubes = combination.split(',')
            for cube in cubes:
                cube = cube.strip()
                cube_count, cube_color = cube.split(' ')
                if game_number not in games:
                    games[game_number] = {}
                if i not in games[game_number]:
                    games[game_number][i] = {}
                games[game_number][i][cube_color] = int(cube_count)

    return games

def solve_puzzle(input: str):
    games = parse_input(input)

    red = 12
    green = 13
    blue = 14

    sum_game_ids = 0
    for game_id, game_combinations in games.items():
        possible = True
        for _, cube_combinations in game_combinations.items():
            cube_combinations = dict({'red':0, 'green':0, 'blue':0}, **cube_combinations)
            if cube_combinations['red'] > red or \
               cube_combinations['green'] > green or \
               cube_combinations['blue'] > blue:
                possible = False 
                break

        if possible:
            sum_game_ids += game_id

    return sum_game_ids

if __name__ == '__main__':
    # test
    input, output = get_puzzle_test_input()
    test_puzzle(input, output)

    # exit()

    # real example
    input = get_puzzle_input('https://adventofcode.com/2023/day/2/input')
    output = solve_puzzle(input)
    print('')
    print("The answer is", output)
    print('')
