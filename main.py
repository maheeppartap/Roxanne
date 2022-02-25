import chess
import chess.svg
import Board
from threading import Thread

import Opponent
import Search.RandomMove


def game_loop(b, opponent):
    while not b.check_stalemate():
        move = input("Enter your move: ")
        try:
            b.make_move_in_board(move)
        except ValueError:
            print("Illegal move, try again")
            continue
        opponent.make_move(b)


if __name__ == '__main__':
    b = Board.Board()

    search_algo = Search.RandomMove.RandomMove()
    op = Opponent.Opponent(search_algo=search_algo, search_heuristic=None, board=b)
    # Seperate the logic from rendering engine
    thread1 = Thread(target=game_loop, args=(b, op))
    # Thread 1 runs the logic, main thread will run the render
    thread1.start()
    b.print_state()
    thread1.join()