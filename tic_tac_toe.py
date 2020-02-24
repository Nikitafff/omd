from itertools import chain
class Board:
    def __init__(self, size):
        self.size = size
        self.desk = {}
        self.cols = None
    
    def init_board(self) -> None:
        for column in range(self.size):
            self.desk.update([(chr(65+column).lower() + str(i + 1), ".") for i in range(self.size)])
        self.cols = list(dict.fromkeys([list(self.desk.keys())[x][0] for x, y in enumerate(self.desk.keys())]))

    def print_board(self):
        row = list(map(str, list(range(1, len(self.cols)+1))))
        for key, value in self.desk.items():
            print(int(key[-1]))
            row.insert(int(key[-1]), value)

        #row.insert()
        print(row)
        board = "  %s\n%s" % ("   ".join(self.cols), "\n".join(row))
        print(board)





board = Board(3)
board.init_board()
board.print_board()
