import tkinter as tk
from tkinter import messagebox


class RegisterScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Titel bovenaan
        title_label = tk.Label(self, text="Account aanmaken",
                               font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Formulierframe
        form = tk.Frame(self)
        form.pack(padx=40, pady=10, fill="x")

        self.fields = {}
        self.errors = {}

        field_definitions = [
            ("first_name", "Voornaam"),
            ("last_name", "Achternaam"),
            ("street", "Straat + huisnummer"),
            ("postcode", "Postcode"),
            ("city", "Woonplaats"),
            ("email", "E-mailadres"),
            ("phone", "Telefoonnummer"),
            ("password", "Wachtwoord"),
            ("password_confirm", "Wachtwoord (bevestiging)"),
        ]

        row = 0
        for field_key, field_label in field_definitions:
            # Label
            label = tk.Label(form, text=field_label)
            label.grid(row=row, column=0, sticky="w", pady=(5, 0))
            row += 1

            # Entry
            entry = tk.Entry(form, show="*" if "password" in field_key else "")
            entry.grid(row=row, column=0, sticky="ew")
            form.grid_columnconfigure(0, weight=1)
            self.fields[field_key] = entry
            row += 1

            # Error label
            error_label = tk.Label(form, text="", fg="red", font=("Arial", 8))
            error_label.grid(row=row, column=0, sticky="w")
            self.errors[field_key] = error_label
            row += 1

        # Knop "Account aanmaken"
        submit_btn = tk.Button(
            self,
            text="Account aanmaken",
            font=("Arial", 14, "bold"),
            bg="#ff8800",
            fg="white",
            activebackground="#ff9900",
            activeforeground="white",
            command=self.on_submit
        )
        submit_btn.pack(pady=20, ipadx=10, ipady=5)

        # Link naar inlogscherm
        link_label = tk.Label(
            self,
            text="Al een account? Inloggen",
            fg="blue",
            cursor="hand2"
        )
        link_label.pack()
        link_label.bind("<Button-1>", lambda e: controller.show_frame("LoginScreen"))


    def clear_errors(self):
        for lbl in self.errors.values():
            lbl.config(text="")

    def on_submit(self):
        self.clear_errors()

        data = {k: v.get().strip() for k, v in self.fields.items()}
        valid = True

        # verplicht
        for key, value in data.items():
            if not value:
                self.errors[key].config(text="Dit veld is verplicht.")
                valid = False

        password = data.get("password", "")
        password_confirm = data.get("password_confirm", "")

        # wachtwoordregels
        if password and len(password) < 8:
            self.errors["password"].config(
                text="Wachtwoord moet minimaal 8 tekens bevatten."
            )
            valid = False

        if password != password_confirm:
            self.errors["password_confirm"].config(
                text="Wachtwoord en bevestiging komen niet overeen."
            )
            valid = False

        if not valid:
            return

        messagebox.showinfo(
            "Account aangemaakt",
            "Je account is aangemaakt.\nJe wordt nu doorgestuurd naar het inlogscherm."
        )

        self.controller.show_frame("LoginScreen")


