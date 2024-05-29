import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.game_mode = tk.StringVar(value="2")
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [[tk.Button(self.root, text='', font='normal 20 bold', width=5, height=2, command=lambda r=r, c=c: self.click(r, c)) for c in range(3)] for r in range(3)]
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].grid(row=r, column=c)

        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        game_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Game", menu=game_menu)
        game_menu.add_radiobutton(label="Two Players", variable=self.game_mode, value="2")
        game_menu.add_radiobutton(label="Single Player", variable=self.game_mode, value="1")
        game_menu.add_separator()
        game_menu.add_command(label="Restart", command=self.reset_board)
        game_menu.add_command(label="Exit", command=self.root.quit)

    def click(self, row, col):
        if self.board[row][col] == '' and self.check_winner() is None:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            winner = self.check_winner()
            if winner:
                self.end_game(winner)
            elif self.is_board_full():
                self.end_game("Tie")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.game_mode.get() == "1" and self.current_player == 'O':
                    self.computer_move()

    def computer_move(self):
        empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == '']
        row, col = random.choice(empty_cells)
        self.click(row, col)

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                return row[0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return self.board[0][2]
        return None

    def is_board_full(self):
        return all(self.board[r][c] != '' for r in range(3) for c in range(3))

    def end_game(self, winner):
        if winner == "Tie":
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        else:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
        self.reset_board()

    def reset_board(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text='')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

