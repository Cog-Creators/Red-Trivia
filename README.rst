==========
Red-Trivia
==========

Warning: The trivia files have moved back to the main repository. (https://github.com/Cog-Creators/Red-DiscordBot)

The trivia files for Red-DiscordBot.

====================================
Moving Red V2 trivia files to Red V3
====================================

Trivia files in Red V3 need to be in the YAML format. To convert your old trivia
files for use in Red V3 use the trivia-yaml library by `Tobotimus <https://github.com/Tobotimus/trivia-yaml>`_.


Installation
============
::

    pip install trivia-yaml


Instructions
=====
Converting a single trivia list::

    trivia-yaml mylist.txt

Converting a folder containing multiple trivia lists::

    trivia-yaml mylists

By default these commands output ``.yaml`` files to a sub-directory named ``yaml_output``.

For outputting files to a particular folder::

    trivia-yaml mylists -t my_output_folder
