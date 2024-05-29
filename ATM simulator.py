import tkinter as tk
from tkinter import messagebox

class ATM_GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ATM Simulator")
        self.geometry("300x200")
        self.balance = 1000  # Initial balance
        self.create_widgets()

    def create_widgets(self):
        self.balance_label = tk.Label(self, text=f"Balance: ${self.balance}")
        self.balance_label.pack(pady=10)

        self.withdraw_button = tk.Button(self, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

        self.deposit_button = tk.Button(self, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.exit_button = tk.Button(self, text="Exit", command=self.quit)
        self.exit_button.pack()

    def withdraw(self):
        amount = float(input("Enter withdrawal amount: $"))
        if amount <= 0:
            messagebox.showerror("Error", "Invalid amount.")
        elif amount > self.balance:
            messagebox.showerror("Error", "Insufficient funds.")
        else:
            self.balance -= amount
            self.update_balance()

    def deposit(self):
        amount = float(input("Enter deposit amount: $"))
        if amount <= 0:
            messagebox.showerror("Error", "Invalid amount.")
        else:
            self.balance += amount
            self.update_balance()

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance}")

if __name__ == "__main__":
    app = ATM_GUI()
    app.mainloop()
