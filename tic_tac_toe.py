from collections import Counter


class Board:
    players = {
        1: "X",
        -1: "O"
    }
    size = {
        "standard": 3
    }

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
        rows_size = sorted(list(range(1, self.size + 1))*3)
        x = 0
        for key, value in self.desk.items():
            row.insert(row.index(key[-1]) + rows_size[x], value)
            x += 1
        tic_toe = "    %s\n" % ("  ".join(self.cols))
        for x in range(1, len(self.cols) + 1):
            tic_toe += ' %s\n' % ('  '.join(row[row.index(str(x)):int(row.index(str(x))) + self.size + 1]))
        print(tic_toe)

    def take_turn(self, player):
        turn = None
        while turn not in self.desk.keys():
            turn = input("Wrie you turn. Example:a1\n")
        while self.desk[turn] == ".":
            self.desk[turn] = Board.players[player]

    def check_winner(self):
        for x in range(0, self.size * self.size, self.size):
            win1 = Counter(list(self.desk.values())[x: x + self.size])
            del win1["."]
            if self.size in win1.values():
                return True
        win2 = Counter(list(self.desk.values())[0::self.size])
        del win2["."]
        if self.size in win2.values():
            return True
        win3 = Counter(list(self.desk.values())[0::self.size**2//2])
        del win3["."]
        if self.size in win3.values():
            return True

    def gameplay(self):
        print("Lets play Tic-tac-toe.Hope you have any friends to play with!")
        self.init_board()
        phase = list(board.players.keys())[0]
        while not self.check_winner():
            self.print_board()
            board.take_turn(phase)
            phase = -phase
        print("Game over!")
        self.print_board()


if __name__ == "__main__":
    board = Board(Board.size['standard'])
    board.gameplay()
