import chess
import chess.svg
import time
import Board
from threading import Thread
from Heuristic import MaterialAdvantage

import Opponent
import Search.RandomMove
import Search.IDA_star
from Heuristic import SpaceAdvantage
from Heuristic import NumberOfChecks

def game_loop(b, opponent, opponent1):
    while not b.check_stalemate():
        # move = input("Enter your move: ")
        confirm_next_move = input("Press enter for opp to make next move")
        print()
        try:
            opponent.make_move(b)
            # b.make_move_in_board(move)
            if b.is_game_over():
                if b.is_checkmate():
                    print("White wins by checkmate!")
                    return 1
                else:
                    print("Game over: Draw after white's move")
                    return -1
        except ValueError:
            print("Opponent: Illegal move, try again")
            continue
        # time.sleep(1)
        confirm_next_move = input("Press enter for opp to make next move")
        try:
            opponent1.make_move(b)
            if b.is_game_over():
                if b.is_checkmate():
                    print("Black wins by checkmate!")
                    return 0
                else:
                    print("Game over: Draw after black's move")
                    return -1
        except ValueError:
            print("Opponent1: Illegal move, try again")
            continue
        # time.sleep(1)


if __name__ == '__main__':
    b = Board.Board()

    opp_heur = MaterialAdvantage.MaterialAdvantage(b)
    search_algo1 = Search.IDA_star.IDA_star(node_expansion=None, heuristic=opp_heur, depth=1)
    opp = Opponent.Opponent(search_algo=search_algo1, search_heuristic=opp_heur, board=b)

    opp1_heur = NumberOfChecks.NumberOfChecks(b)
    search_algo2 = Search.IDA_star.IDA_star(node_expansion=None, heuristic=opp1_heur, depth=1)
    opp1 = Opponent.Opponent(search_algo=search_algo2, search_heuristic=opp1_heur, board=b)

    # Seperate the logic from rendering engine
    thread1 = Thread(target=game_loop, args=(b, opp, opp1))
    # Thread 1 runs the logic, main thread will run the render
    thread1.start()
    b.print_state()
    thread1.join()
