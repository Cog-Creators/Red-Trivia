from pathlib import Path
from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)

__all__ = ['lists']


def lists():
    lists_dir = Path(__file__).parent.resolve() / 'lists'
    return lists_dir.glob("*.yaml")
