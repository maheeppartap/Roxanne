import chess
import Board
import Heuristic


class MaterialAdvantage(Heuristic.Heuristic):
    def __init__(self, board: Board.Board):
        super().__init__(board=board)
        self.MATERIAL_VALUES = {'p': 1, 'P': 1, 'n': 3, 'N': 3, 'b': 3, 'B': 3, 'r': 5, 'R': 5, 'q': 9, 'Q': 9}

    def score(self, board: Board.Board):
        return self.compute_material_advantage(board)

    def compute_material_advantage(self, board: Board.Board):
        active_pieces = board.get_active_pieces()
        white_score = 0
        black_score = 0
        for piece_key in active_pieces:
            piece = active_pieces.get(piece_key)
            if piece.piece_type == chess.KING:
                continue
            piece_value = self.MATERIAL_VALUES.get(str(piece))
            if str(piece).isupper():
                white_score += piece_value
            else:
                black_score += piece_value

        if board.get_turn() is chess.WHITE:
            material_advantage = -(white_score - black_score)
        else:
            material_advantage = -(black_score - white_score)
        return material_advantage
