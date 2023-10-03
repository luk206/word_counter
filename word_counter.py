#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Word counter"""
import argparse
from collections import defaultdict
import re


def word_count(filename):
    """returns a dictionary with the number of occurrences of each word"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        # Use a defaultdict to count words
        word_counts = defaultdict(int)

        # Use a regular expression to tokenize words
        words = re.findall(r'\w+', text.lower())

        for word in words:
            word_counts[word] += 1

        return word_counts

    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')
        return word_counts


def print_word_counts(word_counts):
    """prints the number of occurrences of each word"""
    # Sort the words by their occurrences in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Print the sorted word counts
    for word, count in sorted_word_counts:
        print(f'{word}: {count}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Word count of a text file')
    parser.add_argument('filename', type=str, help='Path to the text file')
    args = parser.parse_args()

    counts = word_count(args.filename)
    if counts:
        print_word_counts(counts)
