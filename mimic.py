#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "jodi08 aka Jo Anna Mollman"
# with help from Kano and Ruben

import random
import sys


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it."""
    with open(filename, "r") as f:  # open and read file
        read_mimic = f.read().split()  # split on white space
        mimic_dict = {"": [read_mimic[0]]}  # setting the starting string
        # getting an index number for word as we loop through read file
        for val, word in enumerate(read_mimic):
            if val < len(read_mimic) - 1:  # checking
                if word in mimic_dict:
                    mimic_dict[word].append(read_mimic[val + 1])
                elif word not in mimic_dict:
                    mimic_dict[word] = [read_mimic[val+1]]  # + val = next word
            # if word is key in read_mimic append word as value to key
            # if word is not a key in read_mimic add as key and add next word as value
    # print(mimic_dict)
    return mimic_dict
# need to make this print the word and the word following


def print_mimic(mimic_dict, start_word):
    """Given a previously created mimic_dict and start_word,
    prints 200 random words from mimic_dict as follows:
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process 200 times
    """
    i = 0
    random_word = start_word
    while i < 200:
        if start_word in mimic_dict:
            next_word = random.choice(mimic_dict[start_word])
            random_word += " " + next_word + " "
            start_word = next_word
            i += 1
        else:
            start_word = ""
            i += 1
    print(random_word)


# Provided main(), calls mimic_dict() and print_mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')
    return d


if __name__ == '__main__':
    main()
