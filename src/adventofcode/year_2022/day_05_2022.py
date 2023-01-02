

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2022, 5, 1)
def part_one(input_data: list[str]):
    
    answer = ''

    # Easier to copy than write code parsing
    crate_stack = [
    ['Z','P','B','Q','M','D','N'],
    ['V','H','D','M','Q','Z','L','C'],
    ['G','Z','F','V','D','R','H','Q'],
    ['N','F','D','G','H'],
    ['Q','F','N'],
    ['T','B','F','Z','V','Q','D'],
    ['H','S','V','D','Z','T','M','Q'],
    ['Q','N','P','F','G','M'],
    ['M','R','W','B']
    ]

    # crate_stack = [['N', 'Z'], ['D', 'C', 'M'],['P']]

    # Use pop 0 because its backwards
    # print(crate_stack[1].pop(0))
    # create initial stacks

    instructions = input_data[10:]
    print(instructions)

    for move in instructions:
        num_blocks_to_move = int(move.split('from')[0].split(' ')[1].strip())
        source_to = move.split('from')[1].split('to')
        source = int(source_to[0].strip())-1
        to = int(source_to[1].strip())-1
        # print('move', num_blocks_to_move)
        # print('source', source)
        # print('to', to)

        # can either use slices or pop off stack
        source_blocks=crate_stack[source][:num_blocks_to_move]
        # need to remove blocks after copy
        print('source_blocks', source_blocks)
        source_blocks.reverse()
        crate_stack[to] = source_blocks + crate_stack[to] 
        # these didn't work right
        update_source_stack = crate_stack[source][num_blocks_to_move:]
        crate_stack[source] = update_source_stack
        # print("with remove", crate_stack[source])
        print(crate_stack)
        
    for st in crate_stack:
        print(st)
        answer = answer + st.pop(0)
    # pop item off stack
    # move it to the appro
    if not answer:
        raise SolutionNotFoundException(2022, 5, 1)

    return answer


@register_solution(2022, 5, 2)
def part_two(input_data: list[str]):
    answer = ''

    # Easier to copy than write code parsing
    crate_stack = [
    ['Z','P','B','Q','M','D','N'],
    ['V','H','D','M','Q','Z','L','C'],
    ['G','Z','F','V','D','R','H','Q'],
    ['N','F','D','G','H'],
    ['Q','F','N'],
    ['T','B','F','Z','V','Q','D'],
    ['H','S','V','D','Z','T','M','Q'],
    ['Q','N','P','F','G','M'],
    ['M','R','W','B']
    ]

    # crate_stack = [['N', 'Z'], ['D', 'C', 'M'],['P']]

    # Use pop 0 because its backwards
    # print(crate_stack[1].pop(0))
    # create initial stacks

    instructions = input_data[10:]
    print(instructions)

    for move in instructions:
        num_blocks_to_move = int(move.split('from')[0].split(' ')[1].strip())
        source_to = move.split('from')[1].split('to')
        source = int(source_to[0].strip())-1
        to = int(source_to[1].strip())-1
        # print('move', num_blocks_to_move)
        # print('source', source)
        # print('to', to)

        # can either use slices or pop off stack
        source_blocks=crate_stack[source][:num_blocks_to_move]
        # need to remove blocks after copy
        print('source_blocks', source_blocks)
        # source_blocks.reverse()
        crate_stack[to] = source_blocks + crate_stack[to] 
        # these didn't work right
        update_source_stack = crate_stack[source][num_blocks_to_move:]
        crate_stack[source] = update_source_stack
        # print("with remove", crate_stack[source])
        print(crate_stack)
        
    for st in crate_stack:
        print(st)
        answer = answer + st.pop(0)

    if not answer:
        raise SolutionNotFoundException(2022, 5, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 5)
    part_one(data)
    part_two(data)
