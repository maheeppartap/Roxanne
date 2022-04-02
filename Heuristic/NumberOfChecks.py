import chess
import Board
import Heuristic


class NumberOfChecks(Heuristic.Heuristic):
    def __init__(self, board: Board.Board):
        super().__init__(board=board)

    def score(self, board: Board.Board):
        return self.compute_number_of_checks(board)

    def compute_number_of_checks(self, board: Board.Board):
        return board.num_checks()
