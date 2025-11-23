import tkinter as tk


class NewReservationScreen(tk.Frame):
    def __init__(self, parent, controller, current_user=None):
        super().__init__(parent)
        self.controller = controller
        self.current_user = current_user

        # Titel
        title = tk.Label(self, text="Nieuwe reservering", font=("Arial", 24, "bold"))
        title.pack(pady=20)

        content = tk.Frame(self)
        content.pack(expand=True)

        #
        # --- LINKER KOLOM ---
        #
        left = tk.Frame(content)
        left.grid(row=0, column=0, padx=20)

        tk.Label(left, text="Klantgegevens", font=("Arial", 14, "bold")).pack(anchor="w")

        self.customer_info = tk.Label(left, text="(automatisch geladen na login)")
        self.customer_info.pack(anchor="w", pady=(0,15))

        tk.Label(left, text="Ophaaldatum").pack(anchor="w")
        self.pickup = tk.Entry(left)
        self.pickup.pack(anchor="w")

        tk.Label(left, text="Retourdatum").pack(anchor="w")
        self.return_date = tk.Entry(left)
        self.return_date.pack(anchor="w")

        tk.Label(left, text="Fietsen", font=("Arial", 14, "bold")).pack(anchor="w", pady=(20,0))

        self.fiets_list = tk.Listbox(left, selectmode="multiple", height=6)
        self.fiets_list.pack()
        self.fiets_list.insert("end", "Herenfiets")
        self.fiets_list.insert("end", "Damesfiets")
        self.fiets_list.insert("end", "Elektrische fiets")

        #
        # --- RECHTER Kolom ---
        #
        right = tk.Frame(content)
        right.grid(row=0, column=1, padx=20)

        tk.Label(right, text="Accessoires", font=("Arial", 14, "bold")).pack(anchor="w")

        self.acc1 = tk.Checkbutton(right, text="Kinderzitje")
        self.acc1.pack(anchor="w")

        self.acc2 = tk.Checkbutton(right, text="Fietshelm")
        self.acc2.pack(anchor="w")

        self.acc3 = tk.Checkbutton(right, text="Fietstas")
        self.acc3.pack(anchor="w")

        tk.Label(right, text="Verzekering", font=("Arial", 14, "bold"), pady=10).pack(anchor="w")

        self.insurance_entry = tk.Entry(right)
        self.insurance_entry.pack(anchor="w")

        #
        # --- ONDERKANT ---
        #
        bottom = tk.Frame(self)
        bottom.pack(pady=30)

        self.total = tk.Label(bottom, text="Totaalprijs: € --,--", font=("Arial", 14, "bold"))
        self.total.pack(pady=10)

        tk.Button(bottom, text="Reservering aanmaken", bg="green", fg="white", width=25).pack(pady=10)
        tk.Button(bottom, text="Annuleren", command=lambda: controller.show_frame("StartScreen"), width=25).pack()
