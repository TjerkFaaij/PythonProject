import tkinter as tk
from tkinter import messagebox


class RegisterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Biker - Account aanmaken")
        self.geometry("500x600")
        self.resizable(True, True)

        # Hoofdtitel
        title_label = tk.Label(self, text="Account aanmaken",
                               font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Frame voor het formulier (één kolom)
        form_frame = tk.Frame(self)
        form_frame.pack(padx=40, pady=10, fill="x")

        # Velden-definitie: veldnaam → (labeltekst)
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
            label = tk.Label(form_frame, text=field_label)
            label.grid(row=row, column=0, sticky="w", pady=(5, 0))
            row += 1

            # Entry
            if "password" in field_key:
                entry = tk.Entry(form_frame, show="*")
            else:
                entry = tk.Entry(form_frame)

            entry.grid(row=row, column=0, sticky="ew")
            form_frame.grid_columnconfigure(0, weight=1)
            self.fields[field_key] = entry
            row += 1

            # Error label (leeg, rood)
            error_label = tk.Label(form_frame, text="",
                                   fg="red", font=("Arial", 8))
            error_label.grid(row=row, column=0, sticky="w")
            self.errors[field_key] = error_label
            row += 1

        # Knop "Account aanmaken"
        submit_btn = tk.Button(
            self,
            text="Account aanmaken",
            font=("Arial", 14, "bold"),
            bg="#ff8800",        # opvallende kleur
            fg="white",
            activebackground="#ff9900",
            activeforeground="white",
            command=self.on_submit
        )
        submit_btn.pack(pady=20, ipadx=10, ipady=5)

        # "Link" naar inloggen
        link_label = tk.Label(
            self,
            text="Al een account? Inloggen",
            fg="blue",
            cursor="hand2"
        )
        link_label.pack()
        link_label.bind("<Button-1>", self.go_to_login)

    def clear_errors(self):
        for lbl in self.errors.values():
            lbl.config(text="")

    def on_submit(self):
        """Validaties uitvoeren en reacties tonen."""
        self.clear_errors()
        data = {k: v.get().strip() for k, v in self.fields.items()}
        valid = True

        # Elke veld is verplicht
        for key, value in data.items():
            if not value:
                self.errors[key].config(text="Dit veld is verplicht.")
                valid = False

        # Wachtwoord-validaties alleen controleren als ze niet leeg zijn
        password = data.get("password", "")
        password_confirm = data.get("password_confirm", "")

        if password and len(password) < 8:
            self.errors["password"].config(
                text="Wachtwoord moet minimaal 8 tekens bevatten."
            )
            valid = False

        if password and password_confirm and password != password_confirm:
            self.errors["password_confirm"].config(
                text="Wachtwoord en bevestiging komen niet overeen."
            )
            valid = False

        if not valid:
            return

        # Hier zou je het account in een database opslaan.
        # Voor nu alleen een melding + "redirect" naar inloggen.
        messagebox.showinfo(
            "Account aangemaakt",
            "Je account is aangemaakt.\nJe wordt nu doorgestuurd naar het inlogscherm."
        )
        self.go_to_login()

    def go_to_login(self, event=None):
        # In een later stadium kun je hier het echte inlogscherm openen.
        # Voor nu alleen een print of messagebox.
        print("Hier zou het inlogscherm geopend worden.")
        messagebox.showinfo("Inloggen", "Hier zou nu het inlogscherm openen.")


if __name__ == "__main__":
    app = RegisterApp()
    app.mainloop()
