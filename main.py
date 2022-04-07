import chess
import chess.svg
import time
import csv
import sys
import os
import Board
from threading import Thread
from Heuristic import MaterialAdvantage

import Opponent
import Search.RandomMove
import Search.IDA_star
from Heuristic import SpaceAdvantage
from Heuristic import NumberOfChecks

def game_loop(b, opponent, opponent1):
    f = open('space_vs_num_checks_depth_1.csv', 'a', newline='')
    writer = csv.writer(f)

    # 0: Black win, 1: White win, 2: Draw, 3: Null
    output_value = 3
    while not b.check_stalemate():
        # move = input("Enter your move: ")
        # confirm_next_move = input("Press enter for opp to make next move")
        try:
            opponent.make_move(b)
            # b.make_move_in_board(move)
            if b.is_game_over():
                if b.is_checkmate():
                    print("White wins by checkmate!")
                    output_value = 1
                    break
                else:
                    print("Game over: Draw after white's move")
                    output_value = 2
                    break
        except ValueError:
            print("Opponent: Illegal move, try again")
            continue
        # time.sleep(1)
        # confirm_next_move = input("Press enter for opp to make next move")
        try:
            opponent1.make_move(b)
            if b.is_game_over():
                if b.is_checkmate():
                    print("Black wins by checkmate!")
                    output_value = 0
                    break
                else:
                    print("Game over: Draw after black's move")
                    output_value = 2
                    break
        except ValueError:
            print("Opponent1: Illegal move, try again")
            continue
        # time.sleep(1)

    print("Writing", str(output_value), "to CSV")
    writer.writerow(str(output_value))
    f.close()
    os._exit(1)


if __name__ == '__main__':
    b = Board.Board()

    # opp1_heur = MaterialAdvantage.MaterialAdvantage(b)
    opp1_heur = SpaceAdvantage.SpaceAdvantage(b)
    # opp1_heur = NumberOfChecks.NumberOfChecks(b)
    search_algo1 = Search.IDA_star.IDA_star(node_expansion=None, heuristic=opp1_heur, depth=1)
    # search_algo1 = Search.RandomMove.RandomMove()
    opp1 = Opponent.Opponent(search_algo=search_algo1, search_heuristic=opp1_heur, board=b)

    # opp2_heur = SpaceAdvantage.SpaceAdvantage(b)
    # opp2_heur = MaterialAdvantage.MaterialAdvantage(b)
    opp2_heur = NumberOfChecks.NumberOfChecks(b)
    search_algo2 = Search.IDA_star.IDA_star(node_expansion=None, heuristic=opp2_heur, depth=1)
    # search_algo2 = Search.RandomMove.RandomMove()
    opp2 = Opponent.Opponent(search_algo=search_algo2, search_heuristic=opp2_heur, board=b)

    # Seperate the logic from rendering engine
    thread1 = Thread(target=game_loop, args=(b, opp1, opp2))
    # Thread 1 runs the logic, main thread will run the render
    thread1.start()
    b.print_state()
    thread1.join()
