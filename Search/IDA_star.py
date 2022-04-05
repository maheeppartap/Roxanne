import Search
import Board
import operator
import random


class IDA_star(Search.Search):
    def __init__(self, node_expansion, heuristic, depth: int):
        super().__init__(node_expansion, heuristic)
        self.depth = depth
        self.heuristic = heuristic

    def _decision(self, board: Board.Board, depth: int):
        # Base case, return score, will get it working with Reece's heuristic in another branch once merged into main
        if depth == 0:
            return self.heuristic.score(board)
        possible_moves_list = list(board.legal_moves())

        # This is for debugging purposes
        moves_score_combo = {}

        # Expand tree nodes - room for improvement given too much redundancy
        for move in possible_moves_list:
            board._make_move_in_board(move)
            moves_score_combo[move] = self._decision(board, depth - 1)
            board.undo_move()

        print(f'Scores: {moves_score_combo}')
        max_key = max(moves_score_combo,key=moves_score_combo.get)  # changing this from min to max seems to make AI do the right thing

        # Pick random move from equal scoring moves
        max_entries = {}
        for key in moves_score_combo:
            if moves_score_combo.get(max_key) == moves_score_combo.get(key):
                max_entries[key] = moves_score_combo.get(key)
        max_key = random.choice(list(max_entries))

        if depth == self.depth:
            return max_key, moves_score_combo[max_key]
        return moves_score_combo[max_key]

    def decision(self, board: Board.Board):
        best_move = self._decision(board, self.depth)
        print(f'Best move: {best_move} with score: {best_move[1]}')
        return best_move[0]
