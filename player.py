import axelrod
from axelrod import Player


class Beginner(Player):
    """
    Just a naive player
    Will Cooperate every time
    """

    name = 'Beginner'

    def strategy(self, opponent):
        return 'D'

if __name__ == '__main__':
    strategies = [s() for s in axelrod.demo_strategies]
    strategies.append(Beginner())

    tournament = axelrod.Tournament(strategies)
    results = tournament.play()
    print(results.ranked_names)
