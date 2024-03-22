"""Splitting a dictionary into two lists."""

__author__ = "730408691"


def get_keys(first_dict: dict[str, int]) -> list[str]:
    """List the keys in the input dictionary."""
    first_list: list[str] = list()
    if first_dict == dict():
        return list()
    for key in first_dict:
        first_list.append(key)
    return first_list


def get_values(second_dict: dict[str, int]) -> list[int]:
    """List the values in the input dictionary."""
    second_list: list[int] = list()
    if second_dict == dict():
        return list()
    for value in second_dict:
        second_list.append(second_dict[value])
    return second_list