import math
import random


class MCTSNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.wins = 0

    def ucb1(self, c=1.4):
        if self.visits == 0:
            return float("inf")
        return self.wins / self.visits + c * math.sqrt(
            math.log(self.parent.visits) / self.visits
        )

    def best_child(self):
        return max(self.children, key=lambda x: x.ucb1())

    def expand(self):
        tried_moves = [child.move for child in self.children]
        for move in self.state.get_legal_moves():
            if move not in tried_moves:
                new_state = self.state.clone()
                new_state.play_move(move)
                child = MCTSNode(new_state, parent=self, move=move)
                self.children.append(child)
                return child
        return None

    def simulate(self):
        state = self.state.clone()
        while not state.is_terminal():
            move = random.choice(state.get_legal_moves())
            state.play_move(move)
        return state.get_winner()

    def backpropagate(self, winner):
        self.visits += 1
        if winner == self.state.current_player * -1:
            self.wins += 1
        if self.parent:
            self.parent.backpropagate(winner)
