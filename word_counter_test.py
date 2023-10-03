#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Word counter tests"""
import io
import unittest
import os
from unittest.mock import mock_open, patch
from collections import defaultdict
from word_counter import word_count, print_word_counts


class TestWordCount(unittest.TestCase):
    """TestWordCount"""

    @patch('builtins.open', new_callable=mock_open, read_data='')
    def test_word_count_empty_file(self, mock_file):
        """test_word_count_empty_file"""
        # Test word_count function with an empty file
        filename = "empty_file.txt"

        word_counts = word_count(filename)
        # Verify file open and read operations
        mock_file.assert_called_once_with(filename, 'r', encoding='utf-8')
        mock_file().read.assert_called_once()
        self.assertEqual(word_counts, defaultdict(int))

    def test_word_count_file_with_repeated_word(self):
        """test_word_count_file_with_repeated_word"""
        # Test word_count function with a file containing repeated words
        filename = "repeated_word.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("apple apple apple apple apple")
        expected_output = defaultdict(int)
        expected_output['apple'] = 5

        word_counts = word_count(filename)
        os.remove(filename)
        # Verify the output of word_count
        self.assertEqual(word_counts, expected_output)

    def test_word_count_file_with_text(self):
        """test_word_count_file_with_text"""
        # Test word_count function with a file containing repeated words
        filename = "test_file.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("This is a test file.\nIt contains some words to count.\nWord count test.")
        expected_output = defaultdict(int)
        expected_output['a'] = 1
        expected_output['contains'] = 1
        expected_output['count'] = 2
        expected_output['file'] = 1
        expected_output['is'] = 1
        expected_output['it'] = 1
        expected_output['some'] = 1
        expected_output['test'] = 2
        expected_output['this'] = 1
        expected_output['to'] = 1
        expected_output['word'] = 1
        expected_output['words'] = 1

        word_counts = word_count(filename)
        os.remove(filename)
        # Verify the output of word_count
        self.assertEqual(word_counts, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_word_counts_empty_word_counts(self, mock_stdout):
        """test_print_word_counts_empty_file"""
        word_counts = defaultdict(int)
        expected_output = ""

        print_word_counts(word_counts)
        # Verify the output of word_count
        print_word_counts_output = mock_stdout.getvalue().strip()
        self.assertEqual(print_word_counts_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_word_counts_with_repeated_word(self, mock_stdout):
        """test_print_word_counts_empty_file"""
        word_counts = defaultdict(int)
        word_counts['apple'] = 5
        expected_output = "apple: 5"

        print_word_counts(word_counts)
        # Verify the output of word_count
        print_word_counts_output = mock_stdout.getvalue().strip()
        self.assertEqual(print_word_counts_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_word_counts_file_with_text(self, mock_stdout):
        """test_print_word_counts_empty_file"""
        word_counts = defaultdict(int)
        word_counts['a'] = 1
        word_counts['contains'] = 1
        word_counts['count'] = 2
        word_counts['file'] = 1
        word_counts['is'] = 1
        word_counts['it'] = 1
        word_counts['some'] = 1
        word_counts['test'] = 2
        word_counts['this'] = 1
        word_counts['to'] = 1
        word_counts['word'] = 1
        word_counts['words'] = 1
        expected_output = """count: 2
test: 2
a: 1
contains: 1
file: 1
is: 1
it: 1
some: 1
this: 1
to: 1
word: 1
words: 1"""
        print_word_counts(word_counts)
        # Verify the output of word_count
        print_word_counts_output = mock_stdout.getvalue().strip()
        self.assertEqual(print_word_counts_output, expected_output)


if __name__ == '__main__':
    unittest.main()
