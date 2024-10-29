"""Lab 9: Fuzzy Matching

Implements "comp" function that will provide completions for objects in the current scope.

Completed by Atticus Bross on 2024/11/09 for DS-1043"""
import inspect
from collections import defaultdict


_FUDGE = 1 # comp returns all matches with length >= longest match - fudge


def ngrams(word: str) -> list[str]:
    """Returns a list of n-grams of word for all relevant n, in descending order of n."""
    grams:list=[]
    for length in range(1,len(word)+1):
        for start in range(0,len(word)-length+1):
            grams.append(word[start:start+length])
    return grams

def add_to_index(option: str, index: dict[str, list[str]]) -> None:
    """Adds a valid option to the n-gram index."""
    # [TODO] Add code here to add a word to the index
    pass


def build_index(options: list[str]) -> dict[str, list[str]]:
    """Creates an n-gram index from options.
    The n-gram index will be a dictionary with n-grams as keys, and lists of corrosponding options as values."""
    index = defaultdict(list)
    # [TODO] Add code here to build up the index, using add_to_index
    return index


def fuzzy_pick(query: str, index: dict) -> dict[str,str]:
    """Returns suggestions for valid options based on the query string.
    Suggestions will take the form of a dictionary with suggestions as keys and longest matching ngram as the value"""
    suggestions = {}
    # [TODO] Add code here to create a dictionary of suggestions
    return suggestions


def comp(query: str, dunders=False) -> None:
    """Provides completions for all objections in the current Python REPL session.
    By default, objects starting with underscores are excluded, but this behavior can be adjusted by passing dunders=True"""
    options = dict(inspect.getmembers(inspect.stack()[len(inspect.stack()) - 1][0]))["f_globals"]
    targets = [obj + '.' + attr
               for obj in options.keys()
               for attr in dir(options[obj])
               if dunders or not (obj.startswith('_')
                                  or attr.startswith('_'))]
    index = build_index(targets)
    suggestions = fuzzy_pick(query, index)
    sorted_suggestions = sorted(suggestions.keys(), key=lambda x: len(suggestions[x]), reverse=True)
    longest_match = len(suggestions[sorted_suggestions[0]])
    for suggestion in sorted_suggestions:
        if len(suggestions[suggestion]) >= longest_match - _FUDGE:
            print(suggestion, '(' + suggestions[suggestion] + ')')
