#!/usr/bin/env python3

def initials(name):
    if not isinstance(name, str):
        raise TypeError('name must be a string')
    return ''.join([c[0] for c in name.split() if c[0].isupper()])

def main():
    '''Main function'''
    print('This program must not crash')
    user_input = [0, 1, 2, 3, 'hello']
    for i in user_input:
        try:  # let's see if it works
            print('1/{} = {}'.format(i, 1/i))
        except ZeroDivisionError as zd_err:  # caught one type of errors
            print('boo: {}'.format(zd_err))
        except TypeError as t_err:  # caught another type of errors
            print('foo: {}'.format(t_err))
        except Exception as err:  # caught all other errors
            print('the end: {}'.format(err))
        finally:  # executed every time, success or failure
            print('we are done here')
    print(initials('United States of America'))
    try:
        print('boo')  # will see this output
        print(initials(2018))
        print('foo')  # won't see this ouput
    except TypeError as t_err:
        print(t_err)

    print('This program did not crash')

if __name__ == '__main__':
    main()
