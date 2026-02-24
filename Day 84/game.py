from board import Board
from player import Player


class Game:

    def __init__(self):
        """Initialize new game with board and players."""
        self.board = Board()

        # Create two players
        self.players = [
            Player("Player 1", "X"),
            Player("Player 2", "O")
        ]

        # Track current player (index 0 or 1)
        self.current_player_index = 0

    @property
    def current_player(self) -> Player:
        """Get the current player object."""
        return self.players[self.current_player_index]

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def play(self):
        """Main game loop."""
        print("\n" + "=" * 40)
        print("   🎮 TIC TAC TOE 🎮")
        print("=" * 40)
        print("\nPlayer 1: X")
        print("Player 2: O")
        print("\nEnter a number (1-9) to place your mark.")

        self.board.display()

        while True:
            # Current player makes a move
            position = self.current_player.get_move()

            # Try to update board
            if self.board.update(position, self.current_player.symbol):
                self.board.display()

                # Check for winner
                winner = self.board.check_winner()
                if winner:
                    print(f"🎉 {self.current_player.name} ({winner}) WINS! 🎉")
                    break

                # Check for draw
                if self.board.is_full():
                    print("It's a DRAW!")
                    break

                # Switch to other player
                self.switch_player()
            else:
                # Cell was already occupied
                print("That cell is already taken! Try again.")

        print("\nThanks for playing!\n")
