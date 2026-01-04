import tkinter as tk
from tkinter import messagebox

def calculate_share():
    try:
        bill_amount = float(bill_entry.get())
        people_count = int(people_entry.get())
        if people_count <= 0:
            raise ValueError("Number of people must be greater than zero.")
        share = bill_amount / people_count
        messagebox.showinfo("Result", f"Each person's share: {share:,.0f} Toman")
    except ValueError:
        messagebox.showwarning("Error", "Please enter valid numbers and make sure number of people is not zero.")

window = tk.Tk()
window.title("Dong Calculator")

tk.Label(window, text="Total Bill (Toman):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
bill_entry = tk.Entry(window)
bill_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Number of People:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
people_entry = tk.Entry(window)
people_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(window, text="Calculate Share", command=calculate_share)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()
