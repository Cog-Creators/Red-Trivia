from pathlib import Path


__all__ = ['lists']


def lists():
    lists_dir = Path(__file__).parent.resolve() / 'lists'
    return lists_dir.glob("*.yaml")
