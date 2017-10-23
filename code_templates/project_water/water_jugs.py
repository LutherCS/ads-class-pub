"""Water jugs project"""
#!/usr/bin/env python3
#encoding: UTF-8


JUG_1_MAX = 4
JUG_2_MAX = 3


class State:
    """State of the jugs"""
    def __init__(self, jug_1, jug_2):
        """state init"""
        self.jug_1 = jug_1
        self.jug_2 = jug_2

    @property
    def jug_1(self):
        '''return jug 1'''
        raise NotImplementedError

    @property
    def jug_2(self):
        '''return jug 2'''
        raise NotImplementedError

    def __eq__(self, other):
        """test if one jug is equal to another"""
        return self.jug_1 == other.jug_1 and self.jug_2 == other.jug_2


    def __str__(self):
        """an easy to understand representation of the state"""
        return '(' + str(self.jug_1) + ', ' + str(self.jug_2) + ')'


    def clone(self):
        """Copy a state"""
        raise NotImplementedError


    def fill_jug_1(self):
        """fill jug1 to capacity from the pump"""
        raise NotImplementedError


    def fill_jug_2(self):
        """fill jug2 to capacity from the pump"""
        raise NotImplementedError


    def empty_jug_1(self):
        """pour the water from jug1 onto the ground"""
        raise NotImplementedError


    def empty_jug_2(self):
        """pour the water from jug2 onto the ground"""
        raise NotImplementedError


    def pour_jug_1_jug_2(self):
        """pour as much water as you can from jug1 to jug2 without spilling"""
        raise NotImplementedError


    def pour_jug_2_jug_1(self):
        """pour as much water as you can from jug2 to jug1 without spilling"""
        raise NotImplementedError

def search(moves_lst, start_state, goal):
    """Find a sequence of states"""
    moves_lst.append(start_state)
    # TODO: Implement recursive search


def main():
    """Main function"""
    print('Measuring Water')
    # 2 gallons in the 4 gallon jar, 0 in the other
    goal = State(2, 0)
    # both jars start out empty
    start = State(0, 0)
    # when search returns, moves will contain the sequence of states
    moves = []
    search(moves, start, goal)
    print([str(s) for s in moves])

if __name__ == "__main__":
    main()
