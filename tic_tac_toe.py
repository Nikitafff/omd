class Board:
    def __init__(self, size):
        self.size = size
        self.desk = {}
    
    def init_board(self) -> None:
        for column in range(self.size):
            self.desk.update([(chr(65+column).lower() + str(i + 1), "") for i in range(self.size)])


board = Board(3)
board.init_board()
print(board.desk)
