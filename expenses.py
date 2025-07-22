import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x500")
root.config(bg="white")

expenses = []

def add_expense():
    desc = desc_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()

    if not desc or not category or not amount:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number.")
        return

    expenses.append((desc, category, amount))
    update_expense_list()
    update_total()
    desc_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def update_expense_list():
    for row in tree.get_children():
        tree.delete(row)
    for i, (desc, category, amount) in enumerate(expenses, start=1):
        tree.insert("", "end", values=(i, desc, category, f"${amount:.2f}"))

def update_total():
    total = sum(amount for _, _, amount in expenses)
    total_label.config(text=f"Total: ${total:.2f}")

def clear_expenses():
    if messagebox.askyesno("Confirm", "Are you sure you want to remove all expenses?"):
        expenses.clear()
        update_expense_list()
        update_total()

# Input Fields
tk.Label(root, text="Description", bg="white").pack()
desc_entry = tk.Entry(root, width=40)
desc_entry.pack()

tk.Label(root, text="Category", bg="white").pack()
category_entry = tk.Entry(root, width=40)
category_entry.pack()

tk.Label(root, text="Amount ($)", bg="white").pack()
amount_entry = tk.Entry(root, width=40)
amount_entry.pack()

# Buttons
add_btn = tk.Button(root, text="Add Expense", command=add_expense, bg="#4CAF50", fg="white")
add_btn.pack(pady=10)

clear_btn = tk.Button(root, text="Remove All Expenses", command=clear_expenses, bg="red", fg="white")
clear_btn.pack(pady=5)

# Expense Table
columns = ("#", "Description", "Category", "Amount")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(pady=10, fill="x")

# Total
total_label = tk.Label(root, text="Total: $0.00", font=("Arial", 12, "bold"), bg="white", fg="green")
total_label.pack(pady=10)

root.mainloop()
