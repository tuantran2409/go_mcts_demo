import random


class RandomPlayer:
    def select_move(self, game):
        return random.choice(game.get_legal_moves())
