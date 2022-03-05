import Board
import Heuristic
import Search


class Opponent:
    def __init__(self, search_algo , search_heuristic , board: Board.Board):
        self.name = "Alice"
        self.search = search_algo
        self.heuristic = search_heuristic
        self.move_stack = []
        self.board = board

    def make_move(self, board):
        self.board = board
        move = self._make_move(board)
        self.board._make_move_in_board(move)


    def _make_move(self, board: Board.Board):
        self.move_stack.append(self.search.decision(board=board))
        return self.move_stack[-1]


