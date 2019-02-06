'''
dice import statement
'''
name = "dice"

from .dice import Cup, Die, FrozenDie

__all__ = ['Cup', 'Die', 'FrozenDie']
