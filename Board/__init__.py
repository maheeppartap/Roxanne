import chess

import Utils


class Board:
    def __init__(self):
        self.board = chess.Board()
        self.moves = []
        pass

    def _legal_moves(self):
        return self.board.legal_moves

    def _num_legal_moves(self):
        return self.board.legal_moves.count()

    def _validate_move(self, move) -> bool:
        return move in self._legal_moves()

    def _make_move(self, move: str) -> bool:
        m = chess.Move.from_uci(move)
        if self._validate_move(m):
            self.board.push(m)
            self.moves.append(m)
            return True
        return False

    def _undo_move(self) -> bool:
        if len(self.moves) == 0:
            return False
        self.board.pop()
        self.moves.pop()
        return True

    def _check_stalemate(self) -> bool:
        return self.board.is_stalemate()

    def _can_claim_fifty_moves(self) -> bool:
        return self.board.can_claim_fifty_moves()

    def _print_state(self):
        app = Utils.QApplication([])
        window = Utils.DisplayState(Gamestate=self.board)
        window.show()
        app.exec()
