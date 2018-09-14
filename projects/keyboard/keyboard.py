'''
Touchscreen Keyboard
'''
#!/usr/bin/env python3

import sys

def spell_check(filename: str) -> None:
    '''Rank words by their proximity to the target'''
    raise NotImplementedError

def main(filename):
    '''Entry point'''
    print('Processing file {}'.format(filename))
    spell_check(filename)
        

if __name__ == '__main__':
    main(sys.argv[1])
