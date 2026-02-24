class Board:

    def __init__(self):
        self.cells = [str(i) for i in range(1, 10)]

    def display(self):
        """The current board state"""
        print("\n")
        for row in range(3):
            # Calculate starting index for each row (0, 3, 6)
            start = row * 3
            # Get three cells for this row
            row_cells = self.cells[start:start + 3]
            # Print formatted row
            print(f"  {row_cells[0]} | {row_cells[1]} | {row_cells[2]}")
            # Print separator (except after last row)
            if row < 2:
                print(" ───┼───┼───")
        print("\n")

    def update(self, position: int, symbol: str) -> bool:
        """
        Place a symbol on the board.

        Args:
            position: Cell number (1-9)
            symbol: 'X' or 'O'

        Returns True if successful, False if cell is occupied
        """
        # Convert position (1-9) to index (0-8)
        index = position - 1

        # Check if cell is available (contains a number, not X/O)
        if self.cells[index] not in ['X', 'O']:
            self.cells[index] = symbol
            return True
        return False

    def is_full(self) -> bool:
        """Check if all cells are occupied (draw condition)"""
        # If any cell is still a number, board is not full
        for cell in self.cells:
            if cell not in ['X', 'O']:
                return False
        return True

    def check_winner(self) -> str | None:
        """Check if there's a winner."""
        winning_lines = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

        for line in winning_lines:
            a, b, c = line
            if self.cells[a] == self.cells[b] == self.cells[c]:
                return self.cells[a]  # Return the winner ('X' or 'O')

        return None  # No winner yet
