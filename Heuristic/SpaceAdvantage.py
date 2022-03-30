import Board
import Heuristic


class SpaceAdvantage(Heuristic.Heuristic):
    def __init__(self, board: Board.Board):
        super().__init__(board=board)

    def score(self, board: Board.Board):
        return self.compute_space_advantage(board)

    def compute_space_advantage(self, board: Board.Board):
        # Defining space advantage as difference of legal moves between players
        legal_moves = board.legal_moves()
        print(legal_moves)
        print("Count: " + str(legal_moves.count()))
        print(type(legal_moves))
        for move in legal_moves:
            print(move)

        board_copy = copy.deepcopy(board)
        board_copy = board_copy.get_mirror()
        return -1
