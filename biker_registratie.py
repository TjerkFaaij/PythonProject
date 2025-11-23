import tkinter as tk
from tkinter import messagebox
import csv
import os


class RegisterScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        title_label = tk.Label(self, text="Account aanmaken",
                               font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

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
            label = tk.Label(form, text=field_label)
            label.grid(row=row, column=0, sticky="w")
            row += 1

            entry = tk.Entry(form, show="*" if "password" in field_key else "")
            entry.grid(row=row, column=0, sticky="ew")
            form.grid_columnconfigure(0, weight=1)
            self.fields[field_key] = entry
            row += 1

            error_label = tk.Label(form, text="", fg="red", font=("Arial", 8))
            error_label.grid(row=row, column=0, sticky="w")
            self.errors[field_key] = error_label
            row += 1

        submit_btn = tk.Button(
            self,
            text="Account aanmaken",
            font=("Arial", 14, "bold"),
            bg="#ff8800",
            fg="white",
            command=self.on_submit
        )
        submit_btn.pack(pady=20)

        link_label = tk.Label(self, text="Al een account? Inloggen",
                              fg="blue", cursor="hand2")
        link_label.pack()
        link_label.bind("<Button-1>", lambda e: controller.show_frame("LoginScreen"))


    def clear_errors(self):
        for lbl in self.errors.values():
            lbl.config(text="")

    #
    # --- CSV OPSLAAN ---
    #
    def save_to_csv(self, data):

        file_exists = os.path.isfile("accounts.csv")

        with open("accounts.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            if not file_exists:
                writer.writerow([
                    "first_name",
                    "last_name",
                    "street",
                    "postcode",
                    "city",
                    "email",
                    "phone",
                    "password"
                ])

            writer.writerow([
                data["first_name"],
                data["last_name"],
                data["street"],
                data["postcode"],
                data["city"],
                data["email"],
                data["phone"],
                data["password"]
            ])


    def on_submit(self):
        self.clear_errors()

        data = {k: v.get().strip() for k, v in self.fields.items()}
        valid = True

        for key, value in data.items():
            if not value:
                self.errors[key].config(text="Dit veld is verplicht.")
                valid = False

        password = data.get("password", "")
        password_confirm = data.get("password_confirm", "")

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

        self.save_to_csv(data)

        messagebox.showinfo(
            "Account aangemaakt",
            "Je account is aangemaakt.\nJe wordt doorgestuurd naar het inlogscherm."
        )

        self.controller.show_frame("LoginScreen")



