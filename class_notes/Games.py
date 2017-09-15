'''Games'''

from abc import ABC, abstractmethod


class Game(ABC):
    def __init__(self, title, pub_date, rating=0, online=False):
        self._title = title
        self._published = pub_date
        self._rating = rating
        self._online = online

    def play(self):
        print('Playing a game: ' + self._title)

    def __str__(self):
        return self._title + ' is a game'

class Electronic(Game):
    @abstractmethod
    def __init__(self, title, pub_date, platform, rating=0, esrb_rating='E', online=False):
        super().__init__(title, pub_date, rating, online)
        self._platform = platform
        self._esrb_rating = esrb_rating

    def __str__(self):
        return super().__str__() + ' available on ' + self._platform

class Tabletop(Game):
    pass


class SingleElectronic(Electronic):
    def __init__(self, title, pub_date, platform, rating=0, esrb_rating='E', online=False):
        super().__init__(title, pub_date, platform, rating, esrb_rating, online)


def main():
    seg = SingleElectronic('StarWars Lego', '2017-09-15', 'Playtation', 10, 'M', True)
    print(seg)

if __name__ == "__main__":
    main()