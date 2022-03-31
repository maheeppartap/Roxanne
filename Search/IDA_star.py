import Search
import Board
import operator


class IDA_star(Search.Search):
    def __init__(self, node_expansion, heuristic, depth: int):
        super().__init__(node_expansion, heuristic)
        self.depth = depth
        self.heuristic = heuristic

    def _decision(self, board: Board.Board, depth: int):
        if depth == 0:
            return self.heuristic.score(board)
        possible_moves_list = list(board.legal_moves())

        moves_score_combo = {}

        # Expand nodes - room for improvement given too much redundancy
        for move in possible_moves_list:
            board._make_move_in_board(move)
            moves_score_combo[move] = self._decision(board, depth - 1)
            board.board.pop()

        max_key = max(moves_score_combo, key=moves_score_combo.get)

        return moves_score_combo[max_key]

    def decision(self, board: Board.Board):
        best_move = self._decision(board, self.depth)
