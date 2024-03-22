"""Summing the elements of a list using different loops."""

_author_ = "730408691"


def w_sum(vals: list[float]) -> float:
    """Taking the sum of a list using a while loop."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Taking the sum of a list using a for loop."""
    sum: float = 0.0
    for idx in vals:
        sum += idx
    return sum
     

def f_range_sum(vals: list[float]) -> float:
    """Taking the sum of a list using a for range loop."""
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum
