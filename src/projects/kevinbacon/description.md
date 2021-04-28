# Six Degrees of Kevin Bacon

Complete the following programming project and submit your source code (as a single archive file) to KATIE.

## Problem

You may have seen the commercial in which Kevin Bacon attempts to cash a check without ID.

<http://www.youtube.com/watch?v=afJRKbBEr2Q>

In this commercial Bacon collects an unlikely combination of people with increasingly tenuous relationships that somehow wind up connecting him with the owner of the store. So you see, he says, "we are practically brothers!" This idea caught on in Hollywood and if you’ve acted in a movie, your _Kevin Bacon number_ is a reflection of how many links away from Kevin Bacon you are.

One actor is linked to another if they have acted in the same movie. For example, Simon Helberg of the _Big Bang Theory_ acted with Gillian Jacobs in _Let it Go_, in 2011. Gillian Jacobs acted with John Malkovich in _Gardens of the Night_ in 2008. John Malkovich acted with Kevin Bacon in _Queens Logic_ in 1991. The idea is nicely described here: [Six Degrees of Kevin Bacon
](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon).

## Task

Your job is to write a program that allows the user to enter the name of an actor and then determines the _Kevin Bacon number_ for that actor. The program should print out the _Kevin Bacon number_ for the actor and both the list of actors that form the chain and the movies they acted in together.

There is one data file for this assignment: movie_actors_full.txt. The format of the file is as follows:

```text
Apokommata (2010)|Leonardo Sfontouris
Apokommata (2010)|Dimitra Kokkori
Apokommata (2010)|Marianna Pouloutiadou
Apokommata (2010)|Dimitra Kokkori
Apokommata (2010)|Anna Etiaridou
Apokrif: Muzyka dlya Petra i Pavla (2005)|Anton Mlodik
Apollo 13 (1995)|Bill Paxton
Apollo 13 (1995)|Gary Sinise
Apollo 13 (1995)|Ed Harris
Apollo 13 (1995)|Tom Hanks
Apollo 13 (1995)|Kevin Bacon
```

## Approach

There are three smaller problems to solve for this assignment.

1. Build a graph that represents the links between all the actors. To build the graph you should use the `Graph` and `Vertex` classes found in the `pythonds3` package. These classes are implemented just like the code in the textbook. **This is the most challenging part of the assignment**. You should start with a small part of the _movies_actors_full.txt_ (e.g. _movies_actors_test.txt_) or create your own test file. You do _not_ want to start with the full file as it contains more than 600,000 lines. With your test file use the Python environment to poke around at the graph and make sure that the links are correct. You will also need to devise a way to keep track of the movie that each actor has in common with her neighbors. _movies_actors_test.txt_ represents the following graph:

   ![Simple graph](kevinbacon.png)

2. Use the _Breadth First Search_ algorithm to create the links from all actors back to _Kevin Bacon_.

3. Write a loop that allows the user to enter a name and see the _Kevin Bacon number_ plus links. You will need to implement the `traverse` function as described in the book to work backward from the actor entered to Kevin Bacon.

Here is an example of the program in action. Your program should produce output that is similar (but not necessarily identical).

```text
> python3 kevinbacon.py
What Actor would you like to trace? (exit to quit) Buster Keaton
Buster Keaton's Kevin Bacon number is 3
1) Buster Keaton acted with Claire Bloom in Limelight (1952)
2) Claire Bloom acted with Kevin Pollak in Max Rose (2013)
3) Kevin Pollak acted with Kevin Bacon in A Few Good Men (1992)
Buster Keaton's Kevin Bacon number is 3
```

## Requirements

- `Vertex` and `Graph` classes are used properly
- User input is processed (keep asking until **exit** is entered)
- Graph is built properly
- Graph is searched properly
- Graph traversal works properly
- Actor(s) with the highest Kevin Bacon number are found

## Grading criteria

1. Pass `test_read_file_vertices`
2. Pass `test_read_file_edges`
3. Pass `test_bfs`
4. Pass `test_traversal`
5. Pass `test_max_kbn`
6. Large file is processed properly
7. Large file is processed within 1 minute
8. User input is processed properly
9. Produced output is correct
10. Application is efficient

## What to do

`python` should be `python3.9` or newer.

- Read _src/projects/kevinbacon/description.md_ (this file).
- Modify _src/projects/kevinbacon/kevinbacon.py_.
- Run _src/projects/kevinbacon/kevinbacon_main.py_.

```bash
python src/projects/kevinbacon/kevinbacon_main.py
```

- Compare your output to that provided in _tests/projects/kevinbacon/kevinbacon_output.txt_.
- Test your implementation.

```bash
python -m pytest tests/projects/kevinbacon/test_kevinbacon.py
```
