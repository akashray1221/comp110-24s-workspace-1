"""Dictionary Unit Tests."""

__author__ = "730408691"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


# Invert Unit Tests
def test_invert_use1() -> None:
    """Test first use case for invert function."""
    library: dict = {"books": "0"}
    library = invert(library)
    new_library: dict = {"0": "books"}
    assert library == new_library


def test_invert_use2() -> None:
    """Test second use case for invert function."""
    library: dict = {"books": "0", "novel": "1"}
    library = invert(library)
    new_library: dict = {"0": "books", "1": "novel"}
    assert library == new_library


def test_invert_edge() -> None:
    """Test edge case for invert function."""
    library: dict = {"books": "0", "novels": "0"}
    with pytest.raises(KeyError):
        invert(library)


# Favorite Color Unit Tests
def test_favorite_color_use1() -> None:
    """Test first use case for favorite color function."""
    rainbow: dict = {"red": "1", "orange": "2", "yellow": "3"}
    rainbow = favorite_color(rainbow)
    new_rainbow: str = "1"
    assert rainbow == new_rainbow


def test_favorite_color_use2() -> None:
    """Test second use case for favorite color function."""
    rainbow: dict = {"green": "4", "sage": "4", "mint": "4"}
    rainbow = favorite_color(rainbow)
    new_rainbow: int = 4
    assert rainbow != new_rainbow


def test_favorite_color_edge() -> None:
    """Test edge case for favorite color function."""
    rainbow: dict = {}
    new_rainbow: str = favorite_color(rainbow)
    assert new_rainbow == ""


# Count Unit Tests
def test_count_use1() -> None:
    """Test first use case for count function."""
    sequence: list = ["1", "10", "100"]
    sequence = count(sequence)
    new_sequence: dict = {"1": 1, "10": 1, "100": 1}
    assert sequence == new_sequence


def test_count_use2() -> None:
    """Test second use case for count function."""
    sequence: list = ["1", "10", "10", "100", "100", "100"]
    sequence = count(sequence)
    new_sequence: dict = {"1": 1, "10": 2, "100": 3}
    assert sequence == new_sequence


def test_count_edge() -> None:
    """Test edge case for count function."""
    sequence: list = []
    sequence = count(sequence)
    assert sequence == {}


# Alphabetizer Unit Tests
def test_alphabetizer_use1() -> None:
    """Test first use case for alphabetizer function."""
    lexicon: list = ["alpha", "beta", "delta"]
    lexicon = alphabetizer(lexicon)
    new_lexicon: dict = {"a": ["alpha"], "b": ["beta"], "d": ["delta"]}
    assert lexicon == new_lexicon


def test_alphabetizer_use2() -> None:
    """Test second use case for alphabetizer function."""
    lexicon: list = ["alpha", "beta", "blockers", "delta"]
    lexicon = alphabetizer(lexicon)
    new_lexicon: dict = {"a": ["alpha"], "b": ["beta", "blockers"], "d": ["delta"]}
    assert lexicon == new_lexicon


def test_alphabetizer_edge() -> None:
    """Test edge case for alphabetizer function."""
    lexicon: list = []
    lexicon = alphabetizer(lexicon)
    assert lexicon == {}


# Attendance Unit Tests
def test_update_attendance_use1() -> None:
    """Test first use case for attendance function."""
    rolecall: dict = {"Thursday": ["Ajay"]}
    today: str = "Thursday"
    students: str = "Priyanka"
    update_attendance(rolecall, today, students)
    new_rolecall: dict = {"Thursday": ["Ajay", "Priyanka"]}
    assert rolecall == new_rolecall


def test_update_attendance_use2() -> None:
    """Test second use case for attendance function."""
    rolecall: dict = {"Thursday": ["Ajay", "Priyanka"]}
    today: str = "Friday"
    students: str = "Aku"
    update_attendance(rolecall, today, students)
    new_rolecall: dict = {"Thursday": ["Ajay", "Priyanka"], "Friday": ["Aku"]}
    assert rolecall == new_rolecall


def test_update_attendance_edge() -> None:
    """Test edge case for attendance function."""
    rolecall: dict = {"Thursday": ["Ajay", "Priyanka"], "Friday": ["Aku"]}
    today: str = "Thursday"
    students: str = "Ajay"
    update_attendance(rolecall, today, students)
    new_rolecall: dict = {"Thursday": ["Ajay", "Priyanka"], "Friday": ["Aku"]}
    assert rolecall == new_rolecall