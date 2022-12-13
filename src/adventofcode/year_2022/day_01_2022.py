

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2022, 1, 1)
def part_one(input_data: list[str]):
    answer = 0
    sums = []
    previousSum = 0
    for i in input_data:
        # print(i)
        if(i == ''):
            sums.append(previousSum)
            previousSum = 0
        else:
            previousSum+=int(i)

    # print(sums)
    sums.sort()
    answer = sums[len(sums)-1]

    if not answer:
        raise SolutionNotFoundException(2022, 1, 1)

    return answer


@register_solution(2022, 1, 2)
def part_two(input_data: list[str]):
    answer = 0
    sums = []
    previousSum = 0
    for i in input_data:
        # print(i)
        if(i == ''):
            sums.append(previousSum)
            previousSum = 0
        else:
            previousSum+=int(i)

    # print(sums)
    sums.sort()
    answer = sums[len(sums)-1]+sums[len(sums)-3]+sums[len(sums)-2]

    if not answer:
        raise SolutionNotFoundException(2022, 1, 1)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 1)
    print(part_one(data))
    part_two(data)
