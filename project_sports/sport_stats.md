
# Sport stats project

## Game class


```python
from collections import Counter

class Game():
    def __init__(self, year, winner, loser, score_w, score_l):
        self._year = year
        self._winner = winner
        self._loser = loser
        self._score_w = score_w
        self._score_l = score_l
    
    @property
    def winner(self):
        return self._winner
    
    def __str__(self):
        return self._winner + " won in " + self._year + " by " + str(self._score_w - self._score_l)
```

## Project idea
1. Open a file
1. Skip the first line
1. Split a line
1. Create a new game object
1. (optional) Update number of titles for the game winner


```python
champions = dict()
all_games = list()
    
with open('nba.txt', 'r') as sport_file:
    sport_file.readline() # ignore the first lint
    for line in sport_file:
        line_items = line.strip().split('\t')
        line_items[2] = line_items[2].split('-')
        g = Game(line_items[0], line_items[1], line_items[3], int(line_items[2][0]), int(line_items[2][1]))
        all_games.append(g)
        champions[g.winner] = champions.get(g.winner, 0) + 1

print("Championship games/series: {}".format(len(all_games)))        
print("Current champions: {}".format(b))
most_successful = Counter(champions).most_common(1)[0]
print("{} is the most successful team with {} titles".format(*most_successful))
```

    Championship games/series: 67
    Current champions: Cleveland Cavaliers won in 2016 by 1
    Boston Celtics is the most successful team with 17 titles



```python

```
