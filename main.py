import chess
import chess.svg
import Board
from threading import Thread
from Heuristic import MaterialAdvantage

import Opponent
import Search.RandomMove
import Search.IDA_star


def game_loop(b, opponent):
    # material_advantage_calc = MaterialAdvantage.MaterialAdvantage(b)
    while not b.check_stalemate():
        # print("Material advantage for player")
        # print(str(material_advantage_calc.score(b)))
        move = input("Enter your move: ")
        try:
            b.make_move_in_board(move)
        except ValueError:
            print("Illegal move, try again")
            continue
        opponent.make_move(b)


if __name__ == '__main__':
    b = Board.Board()
    heur = MaterialAdvantage.MaterialAdvantage(b)
    search_algo = Search.IDA_star.IDA_star(node_expansion=None, heuristic=heur, depth=1)
    op = Opponent.Opponent(search_algo=search_algo, search_heuristic=None, board=b)
    # Seperate the logic from rendering engine
    thread1 = Thread(target=game_loop, args=(b, op))
    # Thread 1 runs the logic, main thread will run the render
    thread1.start()
    b.print_state()
    thread1.join()