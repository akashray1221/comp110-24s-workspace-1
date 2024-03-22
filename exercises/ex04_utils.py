"""List Utilities."""

__author__ = "730408691"


# Part 1 - All
def all(gen_list: list[int], num: int) -> bool:
    """Are all numbers in the list the same as the given number?"""
    idx: int = 0
    result: bool = True
    # Checking for an empty list
    if idx == len(gen_list):
        return (False)
    while (idx < (len(gen_list))):
        if ((gen_list[idx])) == num:
            idx += 1
        else:
            return (False)
    return (result)


# Part 2 - Max
def max(input_list: list[int]) -> int:
    """Find the max value of the list."""
    idx: int = 0
    maximum: int = input_list[0]
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty list")
    while idx < (len(input_list)):
        if (input_list[idx] > maximum):
            maximum = input_list[idx]
        idx += 1
    return (maximum)


# Part 3 - Is_Equal
def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Comparing lists."""
    idx: int = 0
    if (len(first_list) != len(second_list)):
        return False
    while idx < len(first_list):
        if first_list[idx] != second_list[idx]:
            return False
        else:
            idx += 1
    return True


# Part 4 - Extend
def extend(first_list: list[int], second_list: list[int]) -> None:
    """Append the Lists."""
    idx = 0
    while idx < len(second_list):
        first_list.append(second_list[idx])
        idx += 1