"""Dictionary Utility Functions."""

__author__ = "730408691"


# Invert
def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values."""
    output = {}
    for key in input:
        value = input[key]
        if value in output:
            raise KeyError("Duplicate value found for inversion!")
        output[value] = key
    return output


# Fav Colors
def favorite_color(input: dict[str, str]) -> str:
    """Find the favorite color."""
    color_counter: dict[str, int] = {}
    max_value: int = 0
    fav_color: str = ""
    for name in input:
        color = input[name]
        if color in color_counter:
            color_counter[color] += 1
        else:
            color_counter[color] = 1
    for color in color_counter:
        if color_counter[color] > max_value:
            max_value = color_counter[color]
            fav_color = color
    return fav_color


# Count
def count(input: list[str]) -> dict[str, int]:
    """Count values."""
    counter_dict: dict[str, int] = {}
    for item in input:
        if item in counter_dict:
            counter_dict[item] += 1
        else:
            counter_dict[item] = 1
    return counter_dict


# Alphabetizer
def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Organize by alphabetic order."""
    alphabet_list: dict[str, list[str]] = {}
    for word in input:
        first_letter = word[0].lower()
        if first_letter in alphabet_list:
            alphabet_list[first_letter].append(word)
        else:
            alphabet_list[first_letter] = [word]
    return alphabet_list


# Attendance
def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    """Student Attendace."""
    if day in input:
        if student not in input[day]:
            input[day].append(student)
    else:
        input[day] = [student]