import Board
import Search
import random


class RandomMove(Search.Search):
    def __init__(self):
        super().__init__(node_expansion=None, heuristic=None)

    def decision(self, board: Board.Board):
        # super().decision(board)
        possible_moves = board.legal_moves()
        return list(possible_moves)[random.randint(0, len(list(possible_moves)) - 1)]