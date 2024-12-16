import tkinter as tk
from tkinter import messagebox, ttk

class InventoryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.products = {}
        self.low_stock_threshold = 5
        self.users = {"admin": "password123"}
        self.setup_login()

    def setup_login(self):
        self.clear_screen()
        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)
        self.username, self.password = tk.Entry(self.root), tk.Entry(self.root, show="*")
        tk.Label(self.root, text="Username:").pack(); self.username.pack()
        tk.Label(self.root, text="Password:").pack(); self.password.pack()
        tk.Button(self.root, text="Login", command=self.authenticate).pack(pady=10)

    def setup_main(self):
        self.clear_screen()
        tk.Label(self.root, text="Inventory Management System", font=("Arial", 16)).pack(pady=10)
        for text, cmd in [("Add Product", self.add_product_screen), ("View Inventory", self.view_inventory), 
                          ("Generate Report", self.generate_report), ("Logout", self.setup_login)]:
            tk.Button(self.root, text=text, command=cmd).pack(pady=5)

    def authenticate(self):
        if self.users.get(self.username.get()) == self.password.get():
            self.setup_main()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def add_product_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Add Product", font=("Arial", 16)).pack(pady=10)
        entries = [("Product ID", "id"), ("Name", "name"), ("Quantity", "quantity"), ("Price", "price")]
        self.product_entries = {}
        for label, key in entries:
            tk.Label(self.root, text=label + ":").pack()
            self.product_entries[key] = tk.Entry(self.root)
            self.product_entries[key].pack()
        tk.Button(self.root, text="Add", command=self.add_product).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.setup_main).pack(pady=5)

    def add_product(self):
        try:
            product = {
                "id": self.product_entries["id"].get(),
                "name": self.product_entries["name"].get(),
                "quantity": int(self.product_entries["quantity"].get()),
                "price": float(self.product_entries["price"].get()),
            }
            if all(product.values()):
                self.products[product["id"]] = product
                messagebox.showinfo("Success", "Product added successfully!")
                self.add_product_screen()
            else:
                raise ValueError
        except:
            messagebox.showerror("Error", "Invalid input")

    def view_inventory(self):
        self.clear_screen()
        tk.Label(self.root, text="Inventory", font=("Arial", 16)).pack(pady=10)
        tree = ttk.Treeview(self.root, columns=("ID", "Name", "Quantity", "Price"), show="headings")
        for col in ["ID", "Name", "Quantity", "Price"]:
            tree.heading(col, text=col)
        tree.pack(pady=10)
        for p in self.products.values():
            tree.insert("", "end", values=(p["id"], p["name"], p["quantity"], p["price"]))
        tk.Button(self.root, text="Back", command=self.setup_main).pack(pady=5)

    def generate_report(self):
        low_stock = [f"{p['id']} - {p['name']} (Qty: {p['quantity']})" for p in self.products.values() if p["quantity"] <= self.low_stock_threshold]
        report = "\n".join(low_stock) if low_stock else "All products are sufficiently stocked."
        messagebox.showinfo("Low Stock Report", report)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    InventoryManagementSystem(root)
    root.mainloop()
