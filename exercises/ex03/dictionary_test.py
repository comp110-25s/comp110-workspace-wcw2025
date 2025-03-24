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

def test_count_use_2() -> None:
    """Testing count function with non-consecutive repetitions"""
    assert count(['steve','bob','joe','bob','steve']) == {'steve': 2, 'bob': 2, 'joe': 1}

def test_count_empty() -> None:
    """DOCSTRING"""
    assert count([]) == {}

def test_favorite_color_use_1() -> None:
    """Testing favorite_color function without repetitions"""
    assert favorite_color({'a': 'blue', 'b': 'purple', 'c': 'green'}) == 'blue'

def test_favorite_color_use_2() -> None:
    """Testing favorite color function with repetitions"""
    assert favorite_color({'a': 'blue', 'b': 'purple', 'c': 'purple'}) == 'purple'

def test_favorite_color_empty() -> None:
    """DOCSTRING"""
    assert favorite_color({}) == ''

def test_bin_len_use_1() -> None:
    """DOCSTRING"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}

def test_bin_len_use_2() -> None:
    """Testing bin_len function with repetitions"""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}

def test_bin_len_empty() -> None:
    """Testing bin_len function with repetitions"""
    assert bin_len([]) == {}
