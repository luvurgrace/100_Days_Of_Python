class Player:

    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol

    def get_move(self) -> int:  # returns int
        while True:
            try:
                move = input(f"{self.name} ({self.symbol}), enter position (1-9): ")
                move = int(move)

                if 1 <= move <= 9:
                    return move
                else:
                    print("Please enter a number between 1 and 9!")

            except ValueError:
                # Input was not a number
                print("Invalid input! Please enter a number.")
