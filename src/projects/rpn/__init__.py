'''
rpn import statement
'''
name = "rpn"

from .rpn import do_math, postfix_eval

__all__ = ['do_math', 'postfix_eval']
