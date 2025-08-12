import tkinter as tk
import random
from tkinter import messagebox

number = random.randint(1, 100)

def check_guess():
    try:
        guess = int(entry.get())
        if guess < number:
            result_label.config(text="Too low!")
        elif guess > number:
            result_label.config(text="Too high!")
        else:
            result_label.config(text="Correct! 🎉")
            messagebox.showinfo("Success", "You guessed the number!")
    except:
        messagebox.showerror("Error", "Enter a valid number.")

root = tk.Tk()
root.title("Number Guessing Game")

tk.Label(root, text="Guess a number between 1 and 100").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Check", command=check_guess).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
