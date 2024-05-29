import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4")

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password
class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("400x200")
        self.create_widgets()

    def create_widgets(self):
        self.length_label = tk.Label(self, text="Password Length:")
        self.length_label.pack(pady=10)

        self.length_entry = tk.Entry(self, width=10)
        self.length_entry.pack(pady=5)

        self.generate_button = tk.Button(self, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(self, text="", fg="blue", font=("Helvetica", 12, "bold"))
        self.password_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError

            password = generate_password(length)
            self.password_label.config(text=password)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer for password length.")
if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()
