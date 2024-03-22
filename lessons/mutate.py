"""Mutating functions."""

__author__ = "730408691"


def manual_append(gen_list: list[int], num: int) -> None:
    """Manually appending list."""
    gen_list.append(num)


def double(gen_list: list[int]) -> None:
    """Doubling list."""
    x: int = 0
    while x <= (len(gen_list) - 1):
        gen_list[x] *= 2
        x += 1
