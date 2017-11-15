'''Analyze the small movies file'''
#!/usr/bin/env python3
#encoding: UTF-8

class MovieStats():
    '''Movie stats'''
    def __init__(self, filename):
        '''Class constructor'''
        # TODO: Implement the constructor
        raise NotImplementedError

    def read_file(self, filename):
        '''Read the input file'''
        # TODO (optional): read input file and retrieve the necessary data
        raise NotImplementedError

    def get_cast(self, title):
        '''Return all actors who played in a specific movie'''
        # TODO: Write a function that takes a movie title as a parameter and returns names of all actors that played in that movie.
        raise NotImplementedError

    def get_titles_by_year(self, year):
        '''Return a list of all movies released in a certain year'''
        # TODO: Write a function that takes a year as a parameter and returns titles of all movies released that year.
        raise NotImplementedError

    def get_titles_by_cast(self, cast_size):
        '''Return a list of all movies with more actores than cast_size'''
        # TODO: Write a function that takes a number as a parameter and returns titles of all movies with a cast size larger than the specified number.
        raise NotImplementedError

    def get_titles_by_actor(self, name):
        '''Return a list of all movies with a specific actor'''
        # TODO: Write a function that takes a name as a parameter and returns titles of all movies with that featured the specified actor.
        raise NotImplementedError

    def get_most_crowded_movie(self):
        '''Return the movie with the largest cast size'''
        # TODO: Write a function that returns the title of the movie with the largest cast size (the most actors listed).
        raise NotImplementedError

    def get_most_prolific_year(self):
        '''Return the year when the most movies were released'''
        # TODO: Write a function that returns the year when the most titles were released.
        raise NotImplementedError

def main():
    '''Main function'''
    '''Optional. You may use the main function but make sure to pass the tests'''
    movie_info = MovieStats('movie_actors_small.txt')

if __name__ == '__main__':
    main()
