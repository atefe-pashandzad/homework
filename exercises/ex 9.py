import tkinter as tk
from tkinter import messagebox
import csv

file = "contacts.csv"

def load_data():
    data = []
    try:
        with open(file, newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            data = list(reader)
    except FileNotFoundError:
        pass
    return data

def save_data(data):
    with open(file, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Phonebook")
        self.data = load_data()

        tk.Label(root, text="Name:").grid(row=0, column=0)
        self.name = tk.Entry(root)
        self.name.grid(row=0, column=1)

        tk.Label(root, text="Phone:").grid(row=1, column=0)
        self.phone = tk.Entry(root)
        self.phone.grid(row=1, column=1)

        tk.Button(root, text="Add", command=self.add).grid(row=2, column=0, columnspan=2)

        self.listbox = tk.Listbox(root, width=40)
        self.listbox.grid(row=3, column=0, columnspan=2)
        self.show()

        tk.Label(root, text="Search:").grid(row=4, column=0)
        self.search = tk.Entry(root)
        self.search.grid(row=4, column=1)
        tk.Button(root, text="Search", command=self.find).grid(row=5, column=0)
        tk.Button(root, text="Clear", command=self.show).grid(row=5, column=1)

        tk.Button(root, text="Delete", command=self.delete).grid(row=6, column=0, columnspan=2)

        tk.Button(root, text="Sort by Name", command=self.sort_name).grid(row=7, column=0)
        tk.Button(root, text="Sort by Phone", command=self.sort_phone).grid(row=7, column=1)

        tk.Button(root, text="Exit", command=self.exit).grid(row=8, column=0, columnspan=2)

    def show(self, filtered=None):
        self.listbox.delete(0, tk.END)
        data = filtered if filtered else self.data
        for n, p in data:
            self.listbox.insert(tk.END, f"{n} - {p}")

    def add(self):
        n = self.name.get().strip()
        p = self.phone.get().strip()
        if not n or not p:
            messagebox.showwarning("Error", "Enter name and phone")
            return
        if not p.isdigit():
            messagebox.showwarning("Error", "Phone must be digits")
            return
        self.data.append([n, p])
        self.show()
        self.name.delete(0, tk.END)
        self.phone.delete(0, tk.END)

    def find(self):
        q = self.search.get().strip().lower()
        if q:
            filtered = [c for c in self.data if q in c[0].lower() or q in c[1]]
            self.show(filtered)
        else:
            self.show()

    def delete(self):
        sel = self.listbox.curselection()
        if sel:
            confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete?")
            if confirm:
                i = sel[0]
                del self.data[i]
                self.show()
        else:
            messagebox.showwarning("Error", "No contact selected")

    def sort_name(self):
        self.data.sort(key=lambda x: x[0].lower())
        self.show()

    def sort_phone(self):
        self.data.sort(key=lambda x: x[1])
        self.show()

    def exit(self):
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to exit?")
        if confirm:
            save_data(self.data)
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
