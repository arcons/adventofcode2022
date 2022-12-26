from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


def to_number_val(char_val: str):
  # return char_val
  num_val = ord(char_val)
  if(num_val >=97):
    return num_val - 96

  return num_val - 38


@register_solution(2022, 3, 1)
def part_one(input_data: list[str]):
    # plan, bisect the list
    # loop through list and convert to int lists by 1-26 for lower case a-z 27-59 uppercase
    # a 97 ascii 54 difference lowercase
    # A 65 ascii 38 difference uppercase
    # Sort values 
    # Loop through and see if the item exists in both
    # Sum total of values
    sum = 0
    for x in input_data:
      charArray = list(x)
      half_array_length = int(len(charArray)/2)
      first_half = map(to_number_val, charArray[:half_array_length])
      second_half = map(to_number_val, charArray[half_array_length:])
      # print(len(list(first_half)))
      # print(len(list(second_half)))
      # print(list(first_half))
      # print(list(second_half))
      dup = set(list(first_half)) & set(list(second_half))
      for i in dup:
        sum+=i
      # print(list(first_half))


    answer = sum
    # 7712 too low

    if not answer:
        raise SolutionNotFoundException(2022, 3, 1)

    return answer


# @register_solution(2022, 3, 2)
def part_two(input_data: list[str]):
    sum = 0
    for i in range(len(input_data) - 3 + 1):

      # print(input_data[i: i + 3][0], input_data[i: i + 3][1], input_data[i: i + 3][2])
      if(i%3 == 0):
        three = set(list(input_data[i: i + 3][0])) & set(list(input_data[i: i + 3][1])) & set(list(input_data[i: i + 3][2]))
        for w in three:
          print(w)
          sum+=to_number_val(w)

    print(sum)
    answer = sum
    if not answer:
        raise SolutionNotFoundException(2022, 3, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 3)
    # part_one(data)
    part_two(data)
