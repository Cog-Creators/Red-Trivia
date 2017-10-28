from distutils.core import setup
from setuptools import find_packages


def get_requirements():
    with open('requirements.txt') as f:
        reqs = f.readlines()
    return reqs


setup(
    name='Red-Trivia',
    version='0.0.1',
    packages=find_packages(),
    license='GPLv3',
    author='Cog-Creators',
    description='A collection of trivia lists curated by Red-DiscordBot developers',
    install_requires=get_requirements(),
    entry_points={'redbot.trivia': '.core = trivia'}
)
