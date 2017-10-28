from pathlib import Path
from typing import List

from yaml import load, YAMLError

_list_names = None
_loaded_lists = {}


def _lists_dir() -> Path:
    return Path(__file__).parent.resolve() / 'lists'


def _load_list_names():
    lists_dir = _lists_dir()

    lists_paths = lists_dir.glob("*.yaml")

    global _list_names
    _list_names = {p.stem: p.resolve() for p in lists_paths}


def list_names() -> List[str]:
    """
    Enumerates the trivia lists available from this repo.

    Returns
    -------
    list of str
        List of trivia names.
    """
    if _list_names is None:
        _load_list_names()

    # noinspection PyTypeChecker
    return _list_names.keys()


def _load_list(list_name):
    """
    List names must be loaded prior to calling this function.

    Parameters
    ----------
    list_name
    """
    global _loaded_lists

    try:
        _loaded_lists[list_name] = load(_list_names[list_name].open('r'))
    except (KeyError, FileNotFoundError) as e:
        raise FileNotFoundError(
            "There is no list with the name '{}'.".format(list_name)
        ) from e
    except YAMLError as e:
        raise IOError(
            "The list '{}' has malformed data.".format(list_name)
        ) from e


def load_list(list_name: str) -> dict:
    """
    Loads a trivia list.

    Parameters
    ----------
    list_name : str
        One of the names from `list_names`

    Returns
    -------
    dict

    Raises
    ------
    FileNotFoundError
        If the list name doesn't exist or the list file can't be
        found.

    IOError
        If the list can't be loaded.
    """
    if _list_names is None:
        _load_list_names()

    if list_name not in _loaded_lists:
        _load_list(list_name)

    return _loaded_lists[list_name]
