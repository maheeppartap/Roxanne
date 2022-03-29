import chess
import Board


class MaterialAdvantage:
    def __init__(self, board: Board.Board):
        self.board = board
        self.MATERIAL_VALUES = {'p': 1, 'P': 1, 'n': 3, 'N': 3, 'b': 3, 'B': 3, 'r': 5, 'R': 5, 'q': 9, 'Q': 9}

    def compute_material_advantage(self):
        active_pieces = self.board.get_active_pieces()
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

        if self.board.get_turn() is chess.WHITE:
            material_advantage = white_score - black_score
        else:
            material_advantage = black_score - white_score
        return material_advantage
