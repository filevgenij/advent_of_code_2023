import requests

DIGITS = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
    'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

def get_puzzle_input(url):
    cookies = dict(session='3616c7465645f5f13b7afa779027751d5fe355ad05134f32f314ec950f4ed097a749be6824c7418863e171bbcb42695785bc3e21b479ad827050985fbd210b6')
    r = requests.get(url, cookies = cookies)
    return r.text

def get_puzzle_test_input():
    input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
    output = 281
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

def solve_puzzle(input: str):
    lines = input.splitlines()
    calibration_sum = 0
    for line in lines:
        numbers = []

        for i, ch in enumerate(line):
            if ch.isnumeric():
                numbers.append(ch)
            else:
                for text_number, number in DIGITS.items():
                    text_number_len = len(text_number)
                    if line[i:i+text_number_len] == text_number:
                        numbers.append(number)
                        break
            
        if len(numbers) == 2:
            number = int(''.join(numbers))
        elif len(numbers) == 1:
            number = int(''.join(numbers + numbers))
        else:
            number = int(''.join([numbers[0], numbers[len(numbers)-1]]))

        calibration_sum += number

    return calibration_sum


if __name__ == '__main__':
    # test
    input, output = get_puzzle_test_input()
    test_puzzle(input, output)

    # exit()

    # real example
    input = get_puzzle_input('https://adventofcode.com/2023/day/1/input')
    output = solve_puzzle(input)
    print('')
    print("The answer is", output)
    print('')
