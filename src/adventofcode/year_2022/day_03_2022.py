from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2022, 3, 1)
def part_one(input_data: list[str]):
    # plan, bisect the list
    # loop through list and convert to int lists by 1-26 for lower case a-z 27-59 uppercase
    # a 97 ascii 54 difference lowercase
    # A 65 ascii 38 difference uppercase
    # Sort values 
    # Loop through and see if the item exists in both
    # Sum total of values

    print(input_data)
    answer = input_data



    if not answer:
        raise SolutionNotFoundException(2022, 3, 1)

    return answer


# @register_solution(2022, 3, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2022, 3, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 3)
    part_one(data)
    # part_two(data)
