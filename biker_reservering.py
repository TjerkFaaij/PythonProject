import tkinter as tk
from tkinter import messagebox
import csv
import os
import datetime
import uuid


class NewReservationScreen(tk.Frame):
    def __init__(self, parent, controller, current_user=None):
        super().__init__(parent)
        self.controller = controller
        self.current_user = current_user

        title = tk.Label(self, text="Nieuwe reservering", font=("Arial", 24, "bold"))
        title.pack(pady=20)

        content = tk.Frame(self)
        content.pack(expand=True)


        left = tk.Frame(content)
        left.grid(row=0, column=0, padx=20)

        tk.Label(left, text="Klantgegevens", font=("Arial", 14, "bold")).pack(anchor="w")

        self.customer_info = tk.Label(left, text="(automatisch geladen na login)")
        self.customer_info.pack(anchor="w", pady=(0, 15))

        tk.Label(left, text="Ophaaldatum").pack(anchor="w")
        self.pickup = tk.Entry(left)
        self.pickup.pack(anchor="w")

        tk.Label(left, text="Retourdatum").pack(anchor="w")
        self.return_date = tk.Entry(left)
        self.return_date.pack(anchor="w")

        tk.Label(left, text="Fietsen", font=("Arial", 14, "bold")).pack(anchor="w", pady=(20, 0))

        self.fiets_list = tk.Listbox(left, selectmode="multiple", height=6)
        self.fiets_list.pack()
        self.fiets_list.insert("end", "Herenfiets")
        self.fiets_list.insert("end", "Damesfiets")
        self.fiets_list.insert("end", "Elektrische fiets")

        #
        # RIGHT
        #
        right = tk.Frame(content)
        right.grid(row=0, column=1, padx=20)

        tk.Label(right, text="Accessoires", font=("Arial", 14, "bold")).pack(anchor="w")

        self.acc1 = tk.BooleanVar()
        tk.Checkbutton(right, text="Kinderzitje", variable=self.acc1).pack(anchor="w")

        self.acc2 = tk.BooleanVar()
        tk.Checkbutton(right, text="Fietshelm", variable=self.acc2).pack(anchor="w")

        self.acc3 = tk.BooleanVar()
        tk.Checkbutton(right, text="Fietstas", variable=self.acc3).pack(anchor="w")

        tk.Label(right, text="Verzekering", font=("Arial", 14, "bold"), pady=10).pack(anchor="w")
        self.insurance_entry = tk.Entry(right)
        self.insurance_entry.pack(anchor="w")

        #
        # BOTTOM
        #
        bottom = tk.Frame(self)
        bottom.pack(pady=30)

        self.total = tk.Label(bottom, text="Totaalprijs: € --,--", font=("Arial", 14, "bold"))
        self.total.pack(pady=10)

        tk.Button(
            bottom,
            text="Reservering aanmaken",
            bg="green",
            fg="white",
            width=25,
            command=self.make_reservation
        ).pack(pady=10)

        tk.Button(
            bottom,
            text="Annuleren",
            width=25,
            command=lambda: controller.show_frame("StartScreen")
        ).pack()


    #
    # SAVE CSV
    #
    def save_reservation_to_csv(self, data):

        file_exists = os.path.isfile("reservations.csv")

        with open("reservations.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            if not file_exists:
                writer.writerow([
                    "reservation_id",
                    "email",
                    "pickup_date",
                    "return_date",
                    "bikes",
                    "accessories",
                    "insurance",
                    "created"
                ])

            writer.writerow([
                str(uuid.uuid4()),
                data["email"],
                data["pickup"],
                data["return"],
                ",".join(data["bikes"]),
                ",".join(data["accessories"]),
                data["insurance"],
                datetime.datetime.now().isoformat()
            ])


    #
    # ON SUBMIT
    #
    def make_reservation(self):

        email = self.current_user["email"] if self.current_user else ""

        data = {
            "email": email,
            "pickup": self.pickup.get(),
            "return": self.return_date.get(),
            "bikes": [self.fiets_list.get(i) for i in self.fiets_list.curselection()],
            "accessories": [],
            "insurance": self.insurance_entry.get()
        }

        # accessoires
        if self.acc1.get(): data["accessories"].append("Kinderzitje")
        if self.acc2.get(): data["accessories"].append("Fietshelm")
        if self.acc3.get(): data["accessories"].append("Fietstas")

        self.save_reservation_to_csv(data)

        messagebox.showinfo("Succes", "Reservering opgeslagen!")

        self.controller.show_frame("StartScreen")

