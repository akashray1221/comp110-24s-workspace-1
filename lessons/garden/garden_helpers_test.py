"""Test my garden functions."""

__author__ = "730408691"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date
import pytest


def test_add_by_kind_use() -> None:
    """Test use case for add_by_kind function."""
    by_kind: dict = {"tools": ["shovel", "pale"]}
    new_object_kind: str = "tools"
    new_object: str = "hose"
    add_by_kind(by_kind, new_object_kind, new_object)
    new_by_kind: dict = {"tools": ["shovel", "pale", "hose"]}
    assert by_kind == new_by_kind


def test_add_by_kind_edge() -> None:
    """Test edge case for add_by_kind function."""
    by_kind: dict = {"tool": ["shovel", "pale"]}
    new_object_kind: str = "watering"
    new_object: str = "hose"
    add_by_kind(by_kind, new_object_kind, new_object)
    new_by_kind: dict = {"tool": ["shovel", "pale"], "watering": ["hose"]}
    assert by_kind == new_by_kind


def test_add_by_date_use() -> None:
    """Test use case for add_by_date function."""
    resolution_by_month: dict = {"May": ["graduate", "travel"]}
    new_month: str = "June"
    new_resolution: str = "move"
    add_by_date(resolution_by_month, new_month, new_resolution)
    new_resolution_by_month: dict = {"May": ["graduate", "travel"], "June": ["move"]}
    assert resolution_by_month == new_resolution_by_month


def test_add_by_date_edge() -> None:
    """Test use case for add_by_date function."""
    resolution_by_month: dict = {"May": ["graduate", "travel"]}
    new_month: str = "May"
    new_resolution: str = "move"
    add_by_date(resolution_by_month, new_month, new_resolution)
    new_resolution_by_month: dict = {"May": ["graduate", "travel", "move"]}
    assert resolution_by_month == new_resolution_by_month


def test_lookup_by_kind_and_date_use() -> None:
    """Test use case for lookup_by_kind_and_date function."""
    interests_by_kind = {"object": ["shovel", "pale", "hose"], "use": ["digging", "sculpting", "watering"], "cost": ["cheap", "pricy", "expensive"]}
    interests_by_month = {"May": ["shovel", "digging", "cheap"], "June": ["pale", "sculpting", "pricy"], "July": ["hose", "watering", "expensive"]}
    assert lookup_by_kind_and_date(interests_by_kind, interests_by_month, "object", "May") == "objects to plant in May: ['shovel']"


def test_lookup_by_kind_and_date_edge() -> None:
    """Test edge case for lookup_by_kind_and_date function."""
    interests_by_kind = {"object": ["shovel", "pale", "hose"], "use": ["digging", "sculpting", "watering"], "cost": ["cheap", "pricy", "expensive"]}
    interests_by_month = {"May": ["shovel", "digging", "cheap"], "June": ["pale", "sculpting", "pricy"], "July": ["hose", "watering", "expensive"]}
    with pytest.raises(AssertionError):
        lookup_by_kind_and_date(interests_by_kind, interests_by_month, "thing", "May")
