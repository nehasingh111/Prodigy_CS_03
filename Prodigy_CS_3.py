"""Build a tool that assesses the strength of a password based on criteria such as length, 
presence of uppercase and lowercase letters, numbers, and special characters. 
Provide feedback to users on the password's strength."""

import re
import tkinter as tk
from tkinter import messagebox

class PasswordStrengthChecker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Strength Checker")

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.root, show="*", width=50)
        self.password_entry.pack()

        self.strength_label = tk.Label(self.root, text="", fg="black")
        self.strength_label.pack()

        self.show_password_checkbox = tk.BooleanVar()
        self.show_password_checkbox.set(False)
        self.show_password_checkbox_button = tk.Checkbutton(self.root, text="Show Password", variable=self.show_password_checkbox, command=self.toggle_password_visibility)
        self.show_password_checkbox_button.pack()

        self.check_password_button = tk.Button(self.root, text="Check Password Strength", command=self.check_password_strength)
        self.check_password_button.pack()

    def toggle_password_visibility(self):
        if self.show_password_checkbox.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def check_password_strength(self):
        password = self.password_entry.get()
        errors = []

        if len(password) < 12:
            errors.append("Password should be at least 12 characters long")
        if not re.search("[a-z]", password):
            errors.append("Password should contain at least one small letter")
        if not re.search("[A-Z]", password):
            errors.append("Password should contain at least one capital letter")
        if not re.search("[0-9]", password):
            errors.append("Password should contain at least one number")
        if not re.search("[@#$]", password):
            errors.append("Password should contain at least one special character (@, #, $)")

        if errors:
            self.strength_label.config(text="Weak", fg="red")
            error_message = "\n".join(errors)
            messagebox.showerror("Password Errors", error_message)
        else:
            self.strength_label.config(text="Strong", fg="green")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    password_strength_checker = PasswordStrengthChecker()
    password_strength_checker.run()
    