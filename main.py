from go_game import GoGame, BLACK, WHITE
from mcts import MCTSNode
from random_player import RandomPlayer


def mcts_move(game, simulations):
    root = MCTSNode(game)

    for _ in range(simulations):
        node = root

        # Selection
        while node.children:
            node = node.best_child()

        # Expansion
        if not node.state.is_terminal():
            node = node.expand()

        # Simulation
        winner = node.simulate()

        # Backpropagation
        node.backpropagate(winner)

    best = max(root.children, key=lambda x: x.visits)
    return best.move


def play_one_game(simulations):
    game = GoGame()
    random_player = RandomPlayer()

    while not game.is_terminal():
        if game.current_player == BLACK:
            move = mcts_move(game, simulations)
        else:
            move = random_player.select_move(game)
        game.play_move(move)

    return game.get_winner()


def run_statistics(simulations, games=20):
    mcts_win = 0
    random_win = 0
    draw = 0

    for i in range(games):
        winner = play_one_game(simulations)
        if winner == BLACK:
            mcts_win += 1
        elif winner == WHITE:
            random_win += 1
        else:
            draw += 1

    print(f"\nSimulations: {simulations}")
    print(f"MCTS wins  : {mcts_win}")
    print(f"Random wins: {random_win}")
    print(f"Draws     : {draw}")


if __name__ == "__main__":
    for sims in [50, 100, 200]:
        run_statistics(simulations=sims, games=20)
