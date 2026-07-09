import tkinter as tk
from tkinter import messagebox


def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product = {product}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


root = tk.Tk()
root.title("Product Calculator")
root.geometry("300x250")


heading = tk.Label(root, text="Product Calculator", font=("Arial", 14, "bold"))
heading.pack(pady=10)


label1 = tk.Label(root, text="Enter First Number:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack(pady=5)


label2 = tk.Label(root, text="Enter Second Number:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack(pady=5)


btn = tk.Button(root, text="Calculate Product", command=calculate_product)
btn.pack(pady=10)


result_label = tk.Label(root, text="Product = ", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
