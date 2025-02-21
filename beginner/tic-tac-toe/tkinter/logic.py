class TicTacToe:
    def __init__(self):
        """Initialize the game board and set the starting player."""
        self.board = [["" for _ in range(3)] for _ in range(3)]  # 3x3 grid
        self.current_player = "X"  # X always starts first

    def make_move(self, row, col):
        """
        Places the current player's mark at the specified position.
        Returns True if move is valid, False otherwise.
        """
        if self.board[row][col] == "":  # Check if the cell is empty
            self.board[row][col] = self.current_player
            return True
        return False  # Invalid move

    def check_winner(self):
        """
        Checks if there is a winner.
        Returns "X", "O", or "Draw" if game ends, otherwise returns None.
        """
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != "":
                return self.board[i][0]  # Winner in row
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != "":
                return self.board[0][i]  # Winner in column

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != "":
            return self.board[0][0]  # Winner in main diagonal
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != "":
            return self.board[0][2]  # Winner in anti-diagonal

        # Check for draw
        if all(self.board[row][col] != "" for row in range(3) for col in range(3)):
            return "Draw"

        return None  # No winner yet

    def switch_player(self):
        """Switches turn between X and O."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        """Resets the board for a new game."""
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
