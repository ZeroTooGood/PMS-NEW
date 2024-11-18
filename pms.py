import tkinter as tk
from tkinter import messagebox, ttk


class PharmaApp:
    def __init__(self, master):
        self.master = master
        master.title("Pharmaceutical Management System")

        self.drugs = {}
        self.suppliers = {}
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Welcome to Pharmaceutical Management System", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.add_drug_button = tk.Button(self.master, text="Add Drug", command=self.open_add_drug_window)
        self.add_drug_button.pack(pady=10)

        self.view_drugs_button = tk.Button(self.master, text="View Drugs", command=self.open_view_drugs_window)
        self.view_drugs_button.pack(pady=10)

        self.update_drug_button = tk.Button(self.master, text="Update Drug", command=self.open_update_drug_window)
        self.update_drug_button.pack(pady=10)

        self.delete_drug_button = tk.Button(self.master, text="Delete Drug", command=self.open_delete_drug_window)
        self.delete_drug_button.pack(pady=10)

        self.add_supplier_button = tk.Button(self.master, text="Add Supplier", command=self.open_add_supplier_window)
        self.add_supplier_button.pack(pady=10)

        self.view_suppliers_button = tk.Button(self.master, text="View Suppliers",
                                               command=self.open_view_suppliers_window)
        self.view_suppliers_button.pack(pady=10)

        self.update_supplier_button = tk.Button(self.master, text="Update Supplier",
                                                command=self.open_update_supplier_window)
        self.update_supplier_button.pack(pady=10)

        self.delete_supplier_button = tk.Button(self.master, text="Delete Supplier",
                                                command=self.open_delete_supplier_window)
        self.delete_supplier_button.pack(pady=10)

    def open_add_drug_window(self):
        AddDrugWindow(self)

    def open_view_drugs_window(self):
        ViewDrugsWindow(self)

    def open_update_drug_window(self):
        UpdateDrugWindow(self)

    def open_delete_drug_window(self):
        DeleteDrugWindow(self)

    def open_add_supplier_window(self):
        AddSupplierWindow(self)

    def open_view_suppliers_window(self):
        ViewSuppliersWindow(self)

    def open_update_supplier_window(self):
        UpdateSupplierWindow(self)

    def open_delete_supplier_window(self):
        DeleteSupplierWindow(self)


class AddDrugWindow:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master.master)
        self.window.title("Add Drug")

        self.label_name = tk.Label(self.window, text="Drug Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(self.window)
        self.entry_name.pack()

        self.label_quantity = tk.Label(self.window, text="Quantity:")
        self.label_quantity.pack()
        self.entry_quantity = tk.Entry(self.window)
        self.entry_quantity.pack()

        self.label_price = tk.Label(self.window, text="Price:")
        self.label_price.pack()
        self.entry_price = tk.Entry(self.window)
        self.entry_price.pack()

        self.submit_button = tk.Button(self.window, text="Submit", command=self.add_drug)
        self.submit_button.pack(pady=10)

    def add_drug(self):
        name = self.entry_name.get()
        quantity = self.entry_quantity.get()
        price = self.entry_price.get()

        drug_id = len(self.master.drugs) + 1
        self.master.drugs[drug_id] = {"name": name, "quantity": int(quantity), "price": float(price)}

        messagebox.showinfo("Success", "Drug added successfully!")
        self.window.destroy()


class ViewDrugsWindow:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master.master)
        self.window.title("View Drugs")

        self.tree = ttk.Treeview(self.window, columns=("ID", "Name", "Quantity", "Price"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price", text="Price")
        self.tree.pack()

        self.load_data()

    def load_data(self):
        for drug_id, details in self.master.drugs.items():
            self.tree.insert("", tk.END, values=(drug_id, details["name"], details["quantity"], details["price"]))


class UpdateDrugWindow:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master.master)
        self.window.title("Update Drug")

        self.label_id = tk.Label(self.window, text="Drug ID:")
        self.label_id.pack()
        self.entry_id = tk.Entry(self.window)
        self.entry_id.pack()

        self.label_name = tk.Label(self.window, text="New Drug Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(self.window)
        self.entry_name.pack()

        self.label_quantity = tk.Label(self.window, text="New Quantity:")
        self.label_quantity.pack()
        self.entry_quantity = tk.Entry(self.window)
        self.entry_quantity.pack()

        self.label_price = tk.Label(self.window, text="New Price:")
        self.label_price.pack()
        self.entry_price = tk.Entry(self.window)
        self.entry_price.pack()

        self.submit_button = tk.Button(self.window, text="Update", command=self.update_drug)
        self.submit_button.pack(pady=10)

    def update_drug(self):
        drug_id = int(self.entry_id.get())
        if drug_id in self.master.drugs:
            name = self.entry_name.get()
            quantity = self.entry_quantity.get()
            price = self.entry_price.get()

            self.master.drugs[drug_id] = {"name": name, "quantity": int(quantity), "price": float(price)}
            messagebox.showinfo("Success", "Drug updated successfully!")
            self.window.destroy()
        else:
            messagebox.showerror("Error", "Drug ID not found.")


class DeleteDrugWindow:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master.master)
        self.window.title("Delete Drug")

        self.label_id = tk.Label(self.window, text="Drug ID:")
        self.label_id.pack()
        self.entry_id = tk.Entry(self.window)
        self.entry_id.pack()

        self.submit_button = tk.Button(self.window, text="Delete", command=self.delete_drug)
        self.submit_button.pack(pady=10)

    def delete_drug(self):
        drug_id = int(self.entry_id.get())
        if drug_id in self.master.drugs:
            del self.master.drugs[drug_id]
            messagebox.showinfo("Success", "Drug deleted successfully!")
            self.window.destroy()
        else:
            messagebox.showerror("Error", "Drug ID not found.")


class AddSupplierWindow:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master.master)
        self.window.title("Add Supplier")

        self.label_name = tk.Label(self.window, text="Supplier Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(self.window)
        self.entry_name.pack()

        self.label_contact = tk.Label(self.window, text="Contact Info:")
        self.label_contact.pack()
        self.entry_contact = tk.Entry(self.window)
        self.entry_contact.pack()

        self.submit_button = tk.Button(self.window, text="Submit", command=self.add_supplier)
        self.submit_button.pack(pady=10)

    def add_supplier(self):
        name = self.entry_name.get()
        contact_info = self.entry_contact.get()

        supplier_id = len(self.master.suppliers) + 1
        self.master.suppliers[supplier_id] = {"name": name, "contact_info": contact_info}

        messagebox.showinfo("Success", "Supplier added successfully!")
        self.window.destroy()


class ViewSuppliersWindow:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master.master)
        self.window.title("View Suppliers")

        self.tree = ttk.Treeview(self.window, columns=("ID", "Name", "Contact Info"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Contact Info", text="Contact Info")
        self.tree.pack()

        self.load_data()

    def load_data(self):
        for supplier_id, details in self.master.suppliers.items():
            self.tree.insert("", tk.END, values=(supplier_id, details["name"], details["contact_info"]))


class UpdateSupplierWindow:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master.master)
        self.window.title("Update Supplier")

        self.label_id = tk.Label(self.window, text="Supplier ID:")
        self.label_id.pack()
        self.entry_id = tk.Entry(self.window)
        self.entry_id.pack()

        self.label_name = tk.Label(self.window, text="New Supplier Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(self.window)
        self.entry_name.pack()

        self.label_contact = tk.Label(self.window, text="New Contact Info:")
        self.label_contact.pack()
        self.entry_contact = tk.Entry(self.window)
        self.entry_contact.pack()

        self.submit_button = tk.Button(self.window, text="Update", command=self.update_supplier)
        self.submit_button.pack(pady=10)

    def update_supplier(self):
        supplier_id = int(self.entry_id.get())
        if supplier_id in self.master.suppliers:
            name = self.entry_name.get()
            contact_info = self.entry_contact.get()

            self.master.suppliers[supplier_id] = {"name": name, "contact_info": contact_info}
            messagebox.showinfo("Success", "Supplier updated successfully!")
            self.window.destroy()
        else:
            messagebox.showerror("Error", "Supplier ID not found.")


class DeleteSupplierWindow:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master.master)
        self.window.title("Delete Supplier")

        self.label_id = tk.Label(self.window, text="Supplier ID:")
        self.label_id.pack()
        self.entry_id = tk.Entry(self.window)
        self.entry_id.pack()

        self.submit_button = tk.Button(self.window, text="Delete", command=self.delete_supplier)
        self.submit_button.pack(pady=10)

    def delete_supplier(self):
        supplier_id = int(self.entry_id.get())
        if supplier_id in self.master.suppliers:
            del self.master.suppliers[supplier_id]
            messagebox.showinfo("Success", "Supplier deleted successfully!")
            self.window.destroy()
        else:
            messagebox.showerror("Error", "Supplier ID not found.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PharmaApp(root)
    root.mainloop()
