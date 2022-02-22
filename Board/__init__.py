import chess

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

    def validate_move(self, move) -> bool:
        return move in self.legal_moves()

    def make_move(self, move: str) -> bool:
        m = chess.Move.from_uci(move)
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

    def print_state(self):
        app = Utils.QApplication([])
        window = Utils.DisplayState(Gamestate=self.board)
        window.show()
        app.exec()


    # def refresh_screen(self):
        # self.window.paintEvent(None, GameState=self.board)
