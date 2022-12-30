

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


def num_range(inp: str):
    split_range = inp.split('-')
    num_set = set()
    val1 = int(split_range[0])
    val2 = int(split_range[1]) + 1
    for n in range(val1, val2):
        # print(n)
        num_set.add(n)
    return num_set


def maximum(a: int, b: int):
    if a > b:
        return a 
    return b

def min(a: int, b: int):
    if a < b:
        return a 
    return b

@register_solution(2022, 4, 1)
def part_one(input_data: list[str]):

    count = 0
    for i in input_data:
        print(i)
        split = i.split(',')
        # print('split', split)
        first = num_range(split[0])
        second = num_range(split[1])
        minval = min(len(first),len(second))
        # print('first', first)
        # print('second', second)
        intersect_one = first.intersection(second)
        intersect_two = second.intersection(first)
        print('int1', intersect_one)
        if len(intersect_one) == minval or len(intersect_two) == minval:
            print('first + second', first, second)
            count+=1

    answer = count

    if not answer:
        raise SolutionNotFoundException(2022, 4, 1)

    return answer


@register_solution(2022, 4, 2)
def part_two(input_data: list[str]):
    count = 0
    for i in input_data:
        print(i)
        split = i.split(',')
        # print('split', split)
        first = num_range(split[0])
        second = num_range(split[1])
        minval = min(len(first),len(second))
        # print('first', first)
        # print('second', second)
        intersect_one = first.intersection(second)
        intersect_two = second.intersection(first)
        print('int1', intersect_one)
        if len(intersect_one) > 0 or len(intersect_two) > 0:
            print('first + second', first, second)
            count+=1

    answer = count

    if not answer:
        raise SolutionNotFoundException(2022, 4, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 4)
    part_one(data)
    part_two(data)
