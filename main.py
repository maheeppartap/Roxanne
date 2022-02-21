
import Board

if __name__ == '__main__':
    b = Board.Board()
    b._print_state()

    b._make_move("g1f3")
    b._print_state()
