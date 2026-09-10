import tkinter as tk

root = tk.Tk()
root.title("Profile Card")
root.geometry("400x450")
root.configure(bg="lightblue")

card = tk.Frame(root, bg="white", width=300, height=350)
card.pack(pady=40)
card.pack_propagate(False)

profile = tk.Label(
    card,
    text="👤",
    font=("Arial", 60),
    bg="white"
)
profile.pack(pady=15)

name = tk.Label(
    card,
    text="Supratik",
    font=("Arial", 20, "bold"),
    bg="white"
)
name.pack()

profession = tk.Label(
    card,
    text="Python Coder",
    font=("Arial", 14),
    fg="blue",
    bg="white"
)
profession.pack(pady=5)

details = tk.Label(
    card,
    text="supratik/@activityexample\n"
         "📞 01311081469\n"
         "📍 Dhaka",
    font=("Arial", 12),
    bg="white",
    justify="left"
)
details.pack(pady=15)


button = tk.Button(
    card,
    text="Contact Me",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    padx=20,
    pady=5
)
button.pack(pady=10)

root.mainloop()
