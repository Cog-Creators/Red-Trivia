from distutils.core import setup
from pathlib import Path


def get_lists():
    base_dir = Path('redbot/trivia/lists')
    parents = base_dir.parents
    return [str(p.relative_to(parents[0])) for p in base_dir.glob("*.yaml")]


setup(
    name='Red-Trivia',
    version='1.0.2',
    namespace_packages=['redbot'],
    packages=['redbot.trivia'],
    package_data={'redbot.trivia': get_lists()},
    license='GPLv3',
    author='Cog-Creators',
    description='A collection of trivia lists curated by Red-DiscordBot developers'
)
