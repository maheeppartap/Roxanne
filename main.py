import chess
import chess.svg
import Board
from threading import Thread


def game_loop(b):
    print("running!")
    while not b.check_stalemate():
        move = input("Enter your move")
        b.make_move(move)
        # b.print_state()


if __name__ == '__main__':
    b = Board.Board()
    thread1 = Thread(target=game_loop, args=(b,))
    thread1.start()
    b.print_state()
    thread1.join()