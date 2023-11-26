class GoGame:
    def __init__(self):
        self.board = [["." for _ in range(19)] for _ in range(19)]
        self.current_player = "B"

    def switch_player(self):
        self.current_player = "W" if self.current_player == "B" else "B"

    def place_stone(self, row, col):
        if self.board[row][col] == ".":
            self.board[row][col] = self.current_player
            self.switch_player()
        else:
            print("Invalid move: Position already occupied.")

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print("\nCurrent player: " + self.current_player)

    def run(self):
        while True:
            self.print_board()
            try:
                row = int(input("Enter row (0-18): "))
                col = int(input("Enter column (0-18): "))
                if 0 <= row < 19 and 0 <= col < 19:
                    self.place_stone(row, col)
                else:
                    print("Invalid input: Position out of bounds.")
            except ValueError:
                print("Invalid input: Please enter a number.")

if __name__ == "__main__":
    game = GoGame()
    game.run()