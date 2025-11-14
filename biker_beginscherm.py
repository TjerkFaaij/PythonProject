import tkinter as tk

root = tk.Tk()
root.title("Biker")
root.geometry("500x400")
root.resizable(False, False)

# Logo bovenaan
logo_label = tk.Label(root, text="BIKER", font=("Arial", 32, "bold"))
logo_label.pack(pady=40)

# Inloggen-knop
login_btn = tk.Button(
    root,
    text="Inloggen",
    font=("Arial", 16),
    height=2,
    width=20
)
login_btn.pack(pady=10)

# Account aanmaken-knop
register_btn = tk.Button(
    root,
    text="Account aanmaken",
    font=("Arial", 16),
    height=2,
    width=20
)
register_btn.pack(pady=10)

root.mainloop()
