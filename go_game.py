import copy

EMPTY = 0
BLACK = 1
WHITE = -1

BOARD_SIZE = 5


class GoGame:
    def __init__(self):
        self.board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.current_player = BLACK

    def get_legal_moves(self):
        moves = []
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board[i][j] == EMPTY:
                    moves.append((i, j))
        return moves

    def play_move(self, move):
        i, j = move
        if self.board[i][j] != EMPTY:
            return False
        self.board[i][j] = self.current_player
        self.current_player *= -1
        return True

    def is_terminal(self):
        return len(self.get_legal_moves()) == 0

    def get_winner(self):
        black_count = sum(row.count(BLACK) for row in self.board)
        white_count = sum(row.count(WHITE) for row in self.board)
        if black_count > white_count:
            return BLACK
        elif white_count > black_count:
            return WHITE
        return 0

    def clone(self):
        return copy.deepcopy(self)
