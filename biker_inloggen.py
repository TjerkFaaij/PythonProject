import tkinter as tk
from tkinter import messagebox


class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # buitenframe (centreren)
        main = tk.Frame(self)
        main.pack(expand=True)

        # titel
        title = tk.Label(main, text="Inloggen", font=("Arial", 24, "bold"))
        title.pack(pady=20)

        # formulier frame
        form = tk.Frame(main)
        form.pack(pady=10)

        # Email label + entry
        tk.Label(form, text="E-mailadres:").grid(row=0, column=0, sticky="w")
        self.email_entry = tk.Entry(form)
        self.email_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))

        self.email_error = tk.Label(form, text="", fg="red")
        self.email_error.grid(row=2, column=0, sticky="w")

        # Password label + entry
        tk.Label(form, text="Wachtwoord:").grid(row=3, column=0, sticky="w")
        self.password_entry = tk.Entry(form, show="*")
        self.password_entry.grid(row=4, column=0, sticky="ew", pady=(0, 5))

        self.password_error = tk.Label(form, text="", fg="red")
        self.password_error.grid(row=5, column=0, sticky="w")

        # knop inloggen
        login_button = tk.Button(
            main,
            text="Inloggen",
            font=("Arial", 14, "bold"),
            bg="#0066ff",
            fg="white",
            height=2,
            width=18,
            command=self.try_login
        )
        login_button.pack(pady=20)

        # link
        reg_link = tk.Label(main, text="Account aanmaken", fg="blue", cursor="hand2")
        reg_link.pack()
        reg_link.bind("<Button-1>", lambda e: controller.show_frame("RegisterScreen"))

    def clear_errors(self):
        self.email_error.config(text="")
        self.password_error.config(text="")

    def try_login(self):
        self.clear_errors()

        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        valid = True

        if not email:
            self.email_error.config(text="Verplicht veld")
            valid = False

        if not password:
            self.password_error.config(text="Verplicht veld")
            valid = False

        if not valid:
            return

        # -----------------------------------------
        # Hier komt later database-check
        # -----------------------------------------

        # Test inlog:
        if email == "test@mail.com" and password == "test1234":
            messagebox.showinfo("OK", "Inloggen gelukt!")
            self.controller.show_frame("StartScreen")
            return

        self.password_error.config(text="Onjuiste inloggegevens")
