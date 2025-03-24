"""DOCSTRING"""

__author__: str = "730481634"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len

def test_invert_use_1() -> None:
    """DOCSTRING"""
    assert invert({'a': 'z', 'b' : 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}

def test_invert_use_2() -> None:
    """DOCSTRING"""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}

def test_invert_empty() -> None:
    """DOCSTRING"""
    assert invert({}) == {}

def test_count_use_1() -> None:
    """DOCSTRING"""
    assert count(['a','a','a','b','b','b','b','b']) == {'a': 3,'b': 5}