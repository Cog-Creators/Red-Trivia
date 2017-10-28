from distutils.core import setup
from setuptools import find_packages


setup(
    name='Red-Trivia',
    version='0.0.1',
    packages=find_packages(),
    license='GPLv3',
    author='Cog-Creators',
    description='A collection of trivia lists curated by Red-DiscordBot developers',
    entry_points={'redbot.trivia': 'lists = trivia.lists'}
)
