#!/usr/bin/python3
import random
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    """A simple console-based Minesweeper game."""

    def __init__(self, width=10, height=10, mines=10):
        """
        Initialize the Minesweeper game.

        Parameters:
        width (int): The width of the board.
        height (int): The height of the board.
        mines (int): The number of mines to place.
        """
        self.width = width
        self.height = height
        self.total_cells = width * height
        self.mine_count = mines
        self.safe_cells = self.total_cells - self.mine_count  # Total celdas seguras
        self.mines = set(random.sample(range(self.total_cells), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.revealed_safe_cells = 0  # Contador de celdas seguras reveladas

    def print_board(self, reveal=False):
        """Print the current state of the game board."""
        clear_screen()
        print('   ' + ' '.join(f'{i:2}' for i in range(self.width)))
        print('  ' + '-' * (self.width * 3))
        for y in range(self.height):
            print(f'{y:2}|', end='')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print(' * ', end='')  # Imprimir una mina
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(f' {count} ' if count > 0 else '   ', end='')  # Imprimir número o vacío
                else:
                    print(' . ', end='')  # Imprimir celda oculta
            print()
        print('  ' + '-' * (self.width * 3))

    def count_mines_nearby(self, x, y):
        """Count the number of mines adjacent to the given cell."""
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        """
        Reveal the cell at the given coordinates.

        Parameters:
        x (int): The x-coordinate of the cell.
        y (int): The y-coordinate of the cell.

        Returns:
        bool: False if the cell contains a mine, True otherwise.
        """
        if (y * self.width + x) in self.mines:
            return False  # Celda con mina

        if self.revealed[y][x]:  # Evitar volver a revelar una celda ya descubierta
            return True

        self.revealed[y][x] = True
        self.revealed_safe_cells += 1  # Incrementar el contador de celdas seguras reveladas

        # Si la celda no tiene minas cercanas, revelar las celdas vecinas
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)

        return True

    def check_win(self):
        """Check if all safe cells have been revealed."""
        return self.revealed_safe_cells == self.safe_cells

    def play(self):
        """Run the game loop."""
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of bounds. Try again.")
                    continue
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                if self.check_win():
                    self.print_board(reveal=True)
                    print("Congratulations! You cleared the board and won the game!")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
