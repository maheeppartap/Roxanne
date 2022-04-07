import Board
import Heuristic


class SpaceAdvantage(Heuristic.Heuristic):
    def __init__(self, board: Board.Board):
        super().__init__(board=board)

    def score(self, board: Board.Board):
        return self.compute_space_advantage(board)

    def compute_space_advantage(self, board: Board.Board):
        # Defining space advantage as difference of legal moves between players
        num_legal_moves = board.num_legal_moves()
        num_opponent_legal_moves = board.num_opponent_legal_moves()
        return -(num_legal_moves - num_opponent_legal_moves)
