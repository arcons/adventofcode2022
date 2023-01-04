

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day

def isVisible(coordinates: list[list] ,current_x, current_y, direction, currentpos, increment, max_height, max_width):
    currentpos+=increment
    if direction == 'x':
        # print('x direction')
        # print('x direction current', coordinates[current_y][current_x+increment])
        # good opportunity for recursion
        if current_x+currentpos < 0 or current_x+currentpos > max_width-1: 
            return True
        if coordinates[current_y][current_x+currentpos] >= coordinates[current_y][current_x]:

            return False

        return isVisible(coordinates, current_x, current_y, direction, currentpos+increment,increment, max_height, max_width)
    else:
        # print('y direction current', coordinates[current_y][current_x])
        # good opportunity for recursion
        # print('current compare', current_y+currentpos, coordinates[current_y][current_x])
        # not checking edges right
        if current_y+currentpos < 0 or current_y+currentpos > max_height-1: 
            return True
        if coordinates[current_y+currentpos][current_x] >= coordinates[current_y][current_x]:
            return False
            
        return isVisible(coordinates, current_x, current_y, direction , currentpos+increment, increment, max_height, max_width)

    return False

@register_solution(2022, 8, 1)
def part_one(input_data: list[str]):
    answer = 0
    # tree only has to be visible from a given directions
    # loop through each direction x-1, x+1, y-1, y+1
    # loop until 
        # edge is hit in any direction
        # if edge is hit increment
        # a taller tree is found, return false and don't increment
    coordinates = []
    for x in input_data:
        row = []
        for y in list(x):
            row.append(int(y))
        coordinates.append(row)

    # for x in coordinates:
    #     print(x)

    # print(isVisible(coordinates, 3, 3, 'y', 0, -1, len(coordinates), len(coordinates[0])))

    
    for y in range(0, len(coordinates), 1):
        for x in range(0, len(coordinates[0]), 1):
            # compare all directions
            if isVisible(coordinates, x, y, 'x', 0, -1, len(coordinates), len(coordinates[0])):
                if x != 0 and x != 4 and y != 0 and y != 4:
                    print("position is visible with x-1: x:%s , y:%s, %s" % (x, y, coordinates[y][x]))
                answer += 1
            elif isVisible(coordinates, x, y, 'x', 0, 1, len(coordinates), len(coordinates[0])):
                if x != 0 and x != 4 and y != 0 and y != 4:
                    print("position is visible with x+1: x:%s , y:%s, %s" % (x, y, coordinates[y][x]))
                answer += 1
                
            elif isVisible(coordinates, x, y, 'y', 0, -1, len(coordinates), len(coordinates[0])):
                if x != 0 and x != 4 and y != 0 and y != 4:
                    print("position is visible with y-1: x:%s , y:%s, %s" % (x, y, coordinates[y][x]))
                answer += 1

            elif isVisible(coordinates, x, y, 'y', 0, 1, len(coordinates), len(coordinates[0])):
                if x != 0 and x != 4 and y != 0 and y != 4:
                    print("position is visible with y+1: x:%s , y:%s, %s" % (x, y, coordinates[y][x]))
                answer += 1

            

    if not answer:
        raise SolutionNotFoundException(2022, 8, 1)

    return answer


@register_solution(2022, 8, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2022, 8, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 8)
    # 2605 wrong too high
    part_one(data)
    part_two(data)
