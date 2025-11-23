import tkinter as tk
from biker_registratie import RegisterScreen
from biker_inloggen import LoginScreen
from biker_reservering import NewReservationScreen

class BikerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Biker")
        self.geometry("600x600")
        self.resizable(True, True)

        self.container = tk.Frame(self)
        self.container.pack(expand=True)

        self.frames = {}

        # registreer schermen
        for F in (StartScreen, RegisterScreen, LoginScreen, NewReservationScreen):
            frame = F(parent=self.container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartScreen")

    def show_frame(self, name: str):
        frame = self.frames[name]
        frame.tkraise()


class StartScreen(tk.Frame):
    def __init__(self, parent, controller: BikerApp):
        super().__init__(parent)
        self.controller = controller

        main = tk.Frame(self)
        main.pack(expand=True)

        logo = tk.Label(main, text="BIKER", font=("Arial", 32, "bold"))
        logo.pack(pady=40)

        login_btn = tk.Button(
            main,
            text="Inloggen",
            font=("Arial", 16),
            width=20,
            height=2,
            command=lambda: controller.show_frame("LoginScreen")
        )
        login_btn.pack(pady=10)

        register_btn = tk.Button(
            main,
            text="Account aanmaken",
            font=("Arial", 16),
            width=20,
            height=2,
            command=lambda: controller.show_frame("RegisterScreen")
        )
        register_btn.pack(pady=10)


if __name__ == "__main__":
    app = BikerApp()
    app.mainloop()
