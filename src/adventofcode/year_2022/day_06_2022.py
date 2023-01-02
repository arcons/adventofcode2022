

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2022, 6, 1)
def part_one(input_data: list[str]):
    answer = ...

    ## Create a set and empty it if theres a duplicate
    # Or use an empty array and apend each char and clear if the array has the value
    char_arry = list(input_data[0])
    four_char_array = []
    idx = 0
    start_pos = 0
    # for idx, x in enumerate(char_arry):
    while idx < len(char_arry):
        x = char_arry[idx]
        print(idx, x)
        if x not in four_char_array:
            idx = idx + 1
            if len(four_char_array) is 4:
                print(four_char_array)
                return idx-1
            else: 
                four_char_array.append(x)
        else:
            start_pos = start_pos+1
            idx = start_pos
            four_char_array = []
            # four_char_array.append(x)


    if not answer:
        raise SolutionNotFoundException(2022, 6, 1)

    return answer


@register_solution(2022, 6, 2)
def part_two(input_data: list[str]):
    answer = ...

    ## Create a set and empty it if theres a duplicate
    # Or use an empty array and apend each char and clear if the array has the value
    char_arry = list(input_data[0])
    four_char_array = []
    idx = 0
    start_pos = 0
    # for idx, x in enumerate(char_arry):
    while idx < len(char_arry):
        x = char_arry[idx]
        # print(idx, x)
        if len(four_char_array) is 14:
            print(four_char_array)
            return idx
        if x not in four_char_array:
            idx = idx + 1
            four_char_array.append(x)
        else:
            start_pos = start_pos+1
            idx = start_pos
            print(start_pos, len(four_char_array))
            four_char_array = []
            # four_char_array.append(x)
    if not answer:
        raise SolutionNotFoundException(2022, 6, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 6)
    # part_one(data)
    part_two(data)
