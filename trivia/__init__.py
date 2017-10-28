from pathlib import Path
from typing import List

__all__ = ['list_names']

_list_map = None


def _lists_dir() -> Path:
    return Path(__file__).parent.resolve() / 'lists'


def _load_list_names():
    lists_dir = _lists_dir()

    lists_paths = lists_dir.glob("*.yaml")

    global _list_map
    _list_map = {p.stem: p.resolve() for p in lists_paths}


def list_map() -> dict:
    """
    Enumerates the trivia lists available from this repo.

    Returns
    -------
    list of str
        List of trivia names.
    """
    if _list_map is None:
        _load_list_names()

    # noinspection PyTypeChecker
    return _list_map
