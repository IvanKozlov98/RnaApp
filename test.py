import pytest as pytest

from server import Hospital


def test_relative():
    """
        Tests that relative defined rightly
    """
    assert Hospital.is_relative("aaaaa", "aaaaa")
    assert Hospital.is_relative("aaaaaaaaga", "aaaaaaaaaa")
    assert not Hospital.is_relative("tttttttttt", "aaaaaaaaaa")
    assert not Hospital.is_relative("ttttttggtt", "aaaaaaaaaa")


def test_ethnic():
    """
        Tests that checking same ethnic defined rightly
    """
    assert Hospital.is_same_ethnic_group("aaaaa", "aataa")
    assert Hospital.is_same_ethnic_group("aaaaaaaggg", "aaaaaaaaaa")
    assert not Hospital.is_same_ethnic_group("tttttttttt", "aaaaaaaaaa")
    assert not Hospital.is_same_ethnic_group("ttttttggtt", "aaaaaaaaaa")
