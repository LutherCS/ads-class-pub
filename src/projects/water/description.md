# Die Hard with a Water Jug

Complete the following programming project and submit your source code (as a single archive file) to KATIE.

## Problem

Assume you have a 5-gallon jug and a 3-gallon jug. Neither of the jugs has markings on them. There is a pump that can be used to fill the jugs with water. How can you get exactly 4 (four) gallons of water in the 5-gallon jug?

Once you solve this specific problem, see if your solution works for other cases (some other amount of water in either jug; starting with non-empty jugs).

## Approach

The key to this problem is in using something called a _state_. A state represents the amount of water in each of the jugs. You should create a class called `State` or something similar. The `State` class will remember how much water is in each jug.

The solution to this problem will be a list of states. A key to solving this problem recursively is that there are multiple parts to a base case. There is the "good" part where the state you have just created is the same as the goal state. At this point, you should stop the recursion. There is a "bad" part to the base case where the state you have just created is already on the list. You should not pursue this path any further and pass. The general case is a recursive call with an updated list of moves and a new beginning state.

Remember that every state branches into **6** more states, so you may end up with many similar conditions.

To make it clear what you are doing you will want to implement the following methods:

- `__init__` - Initialize the state (specify the amount of water that is initially in each jug). It is particularly important to specify the goal state
- `__eq__` - test if one state is equal to another
- `__str__` - make an easy to understand representation of the state
- `fill_jug_1` - fill jug1 to capacity from the pump
- `fill_jug_2` - fill jug2 to capacity from the pump
- `empty_jug_1` - pour the water from jug1 onto the ground
- `empty_jug_2` - pour the water from jug2 onto the ground
- `pour_jug_1_to_jug_2` - pour as much water as you can from jug1 to jug2 without spilling
- `pour_jug_2_to_jug_1` - pour as much water as you can from jug2 to jug1 without spilling

## Algorithm

1. Base case 1 (stuck): the `start` state is already in the list of moves.
   - Return `None` or `False` - you don't want to keep pouring water from one jug to another
2. Add `start` state to the list of moves
3. Base case 2 (success): the `start` state is the same as the `goal` state
   - Return the list of moves
4. Apply any operation (`fill`, `empty`, `pour`) to the start state and keep searching (recursively) with the new start state, same goal, and the growing list of moves
5. Make sure to apply all 6 operations (`fill jug 1`, `fill jug 2`, `empty jug 1`, `empty jug 2`, `pour from jug 1 to jug 2`, `pour from jug 2 to jug 1`) to the start state and check if any recursive call returns a result.

## Output note

Depending on the chosen approach, your output may deviate from the provided. Don't worry, it's fine, as long as you find **a** path.

## Grading note

A properly implemented `search` function is **50%** of the grade, as indicated by the number of tests provided.

## What to do

`python3` should be `python3.9` or newer.

- Read _src/projects/water/description.md_ (this file).
- Modify _src/projects/water/water.py_.
- Run _src/projects/water/water_main.py_.

```bash
python3 src/projects/water/water_main.py
```

- Compare your output to that provided in _tests/projects/water/water_output.txt_.
- Test your implementation.

```bash
python3 -m pytest tests/projects/water/test_water.py
```

## References

- [Solving the Water Jug Problem | Aakritty](https://aakritty.wordpress.com/2014/02/10/solving-the-water-jug-problem/)
- [The Two Water Jug Puzzle - GeeksforGeeks](https://www.geeksforgeeks.org/two-water-jug-puzzle/)
- [https://www.cs.rochester.edu/u/scott/courses/162/notes/03-recursion](https://www.cs.rochester.edu/u/scott/courses/162/notes/03-recursion)
