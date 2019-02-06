'''
words import statement
'''
name = "words"

from .words import Stack, Queue, read_file, distance, diff_by_one_all

__all__ = ['read_file', 'distance', 'diff_by_one_all']
