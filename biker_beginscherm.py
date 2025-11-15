import tkinter as tk
from biker_registratie import RegisterScreen

class BikerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Biker")
        self.geometry("600x600")
        self.resizable(True, True)

        self.container = tk.Frame(self)
        self.container.pack(expand=True)
        self.frames = {}

        # Registreer alle schermen
        for F in (StartScreen, RegisterScreen):
            frame = F(parent=self.container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Start met beginscherm
        self.show_frame("StartScreen")

    # Wisselt tussen scherm
    def show_frame(self, name: str):
        frame = self.frames[name]
        frame.tkraise()

class StartScreen(tk.Frame):
    def __init__(self, parent, controller: BikerApp):
        super().__init__(parent)
        self.controller = controller

        # Logo bovenaan
        logo_label = tk.Label(self, text="BIKER", font=("Arial", 32, "bold"))
        logo_label.pack(pady=40)

        # Inloggen-knop
        login_btn = tk.Button(
            self,
            text="Inloggen",
            font=("Arial", 16),
            height=2,
            width=20
        )
        login_btn.pack(pady=10)

        # Account aanmaken-knop
        register_btn = tk.Button(
            self,
            text="Account aanmaken",
            font=("Arial", 16),
            height=2,
            width=20,
            command=lambda: controller.show_frame("RegisterScreen")
        )
        register_btn.pack(pady=10)

if __name__ == "__main__":
    app = BikerApp()
    app.mainloop()
