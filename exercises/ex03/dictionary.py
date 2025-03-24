"""Practice creating functions using dictionaries"""

__author__: str = "730481634"

def invert(dictionary: dict[str,str]) -> dict[str,str]:
    """Function inverting a given dictionary's keys and values"""
    inversion: dict[str,str] = {}
    for key in dictionary:
        if dictionary[key] in inversion:
            raise KeyError("You can't have a value more than once!")
        else:
            inversion[dictionary[key]] = key
    return inversion

def count(given_list: list[str]) -> dict[str,int]:
    """Function counting the number of times a value appears in a list"""
    index: int = 0
    final_dict: dict[str,int] = {}
    while index < len(given_list):
        if given_list[index] in final_dict:
            final_dict[given_list[index]] += 1
            index += 1
        else:
            final_dict[given_list[index]] = 1
            index += 1
    return final_dict

def favorite_color(colors: dict[str,str]) -> str:
    """Function determining the most popular answer from a poll of people's favorite colors"""
    color_list: list[str] = []
    for key in colors:
        color_list.append(colors[key])
    counted_colors: dict[str,int] = count(color_list)
    count_list: list[int] = []
    for key in counted_colors:
        count_list.append(counted_colors[key])
    for key in counted_colors:
        if counted_colors[key] == max(count_list):
            return key
    return ''

def bin_len(strings: list[str]) -> dict[int,set[str]]:
    """Function sorting a words into bins by length"""
    idx: int = 0
    bin_sizes: list[int] = []
    while idx < len(strings):
        bin_sizes.append(len(strings[idx]))
        idx += 1
    idx = 0
    bins: dict[int,set[str]] = {}
    while idx < len(bin_sizes):
        if bin_sizes[idx] in bins:
            bins[bin_sizes[idx]].add(strings[idx])
            idx += 1
        else:
            bins[bin_sizes[idx]] = {strings[idx]}
            idx += 1
    return bins