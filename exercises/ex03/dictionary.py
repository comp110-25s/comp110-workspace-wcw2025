"""DOCSTRING"""

__author__: str = "730481634"

def invert(dictionary: dict[str,str]) -> dict[str,str]:
    """Function inverting a given dictionary's keys and values"""
    inversion: dict[str,str] ={}
    for key in dictionary:
        if dictionary[key] in inversion:
            raise KeyError("You can't have a value more than once!")
        else:
            inversion[dictionary[key]]=key
    return inversion

def count(given_list: list[str]) -> int:
    index: int = 0
    while index<len(given_list):
        return 5
    return 5