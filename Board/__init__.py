import chess
import copy

import Utils


class Board:
    def __init__(self):
        self.board = chess.Board()
        self.moves = []
        self.rendered = False
        pass

    def legal_moves(self):
        return self.board.legal_moves

    def num_legal_moves(self):
        return self.board.legal_moves.count()

    def opponent_legal_moves(self):
        self._flip_turn()
        opponent_legal_moves = copy.deepcopy(self.board.legal_moves)
        self._flip_turn()
        return opponent_legal_moves

    def num_opponent_legal_moves(self):
        self._flip_turn()
        num_opponent_legal_moves = self.num_legal_moves()
        self._flip_turn()
        return num_opponent_legal_moves

    def _flip_turn(self):
        try:
            self.board.turn = not self.get_turn()
            return True
        except:
            return False

    def num_checks(self):
        return sum(self.board.checkers().tolist())

    def validate_move(self, move) -> bool:
        return move in list(self.legal_moves())

    def make_move_in_board(self, move: str) -> bool:
        m = chess.Move.from_uci(move)
        if not self.validate_move(m):
            raise ValueError
        return self._make_move_in_board(m)

    def _make_move_in_board(self, m: chess.Move) -> bool:
        if self.validate_move(m):
            self.board.push(m)
            self.moves.append(m)
            return True
        return False

    def undo_move(self) -> bool:
        if len(self.moves) == 0:
            return False
        self.board.pop()
        self.moves.pop()
        return True

    def check_stalemate(self) -> bool:
        return self.board.is_stalemate()

    def can_claim_fifty_moves(self) -> bool:
        return self.board.can_claim_fifty_moves()

    def get_active_pieces(self):
        return self.board.piece_map()

    def get_turn(self):
        return self.board.turn

    def is_game_over(self):
        return self.board.is_game_over()

    def is_checkmate(self):
        return self.board.is_checkmate()

    def print_state(self):
        app = Utils.QApplication([])
        window = Utils.DisplayState(Gamestate=self.board)
        window.show()
        app.exec()

    # def refresh_screen(self):
        # self.window.paintEvent(None, GameState=self.board)
