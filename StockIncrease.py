import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox, Menu
from tkinter import ttk


def display_StockIncrease():
    ################################## Center Frame #####################################################
    StockIncrease_root = Tk()
    StockIncrease_root.title("Stock Increase")
    w = 800
    h = 600
    screenwidth = StockIncrease_root.winfo_screenwidth()
    screenheight = StockIncrease_root.winfo_screenheight()
    x = int((screenwidth - w) / 2)
    y = int((screenheight - h) / 2)
    StockIncrease_root.geometry(f'{w}x{h}+{x}+{y}')
    StockIncrease_root.resizable(False, False)

    StockIncrease_root.configure(bg="#6e1423")
    StockIncrease_root.iconbitmap("project pictures/Blood group.ico")

    lbl = Label(StockIncrease_root, text='Stock (Increase)', font=(
        "Cambria", 40, "bold", "italic"), bg="#6e1423", fg="#f8e5ee")
    lbl.pack(pady=20)

    main_frame = Frame(StockIncrease_root, bg="#6e1423")
    main_frame.pack(pady=20)

    # Frame to hold blood group elements
    blood_group_frame = Frame(main_frame, bg="#6e1423")
    blood_group_frame.pack(side=LEFT, padx=20)

    blood_group_label = Label(blood_group_frame, text="Blood Group", font=(
        "arial", 18, "bold"), fg="#f8e5ee", bg="#6e1423")
    blood_group_label.grid(row=0, column=0, padx=5, pady=5)
    blood_group_combobox = ttk.Combobox(blood_group_frame, values=[
                                        "A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"], font=("Segoe UI", 8), state='readonly')
    blood_group_combobox.grid(row=0, column=1, padx=5, pady=5)

    # Frame to hold units elements
    units_frame = Frame(main_frame, bg="#6e1423")
    units_frame.pack(side=LEFT, padx=20)

    units_label = Label(units_frame, text="Units", font=(
        "arial", 18, "bold"), fg="#f8e5ee", bg="#6e1423")
    units_label.grid(row=0, column=0, padx=5, pady=5)
    units_entry = Entry(units_frame)
    units_entry.grid(row=0, column=1, padx=5, pady=5)

    ########################################### Update Function ######################################
    def update_table():
        # Get selected values from Combobox and Entry
        blood_group = blood_group_combobox.get()
        units = units_entry.get()

        # Validate inputs
        if not blood_group or not units:
            messagebox.showerror("Input Error", "Please fill out both fields")
            return

        try:
            unit_int = int(units)
        except ValueError:
            messagebox.showerror("Input Error", "Units must be an integer")
            return

        con = sqlite3.connect("BloodBank.db")
        cursor = con.cursor()

        cursor.execute(
            "SELECT Units FROM stock WHERE BloodGroup = ?", (blood_group,))
        result = cursor.fetchone()

        if result:
            cursor.execute(
                "UPDATE stock SET Units = Units + ? WHERE BloodGroup = ?", (unit_int, blood_group))
            con.commit()
            messagebox.showinfo("Success", "Successfully updated")

            # Clear the inputs
            blood_group_combobox.set('')
            units_entry.delete(0, 'end')

            # Update the Treeview
            load_data()

        else:
            messagebox.showerror(
                "Input Error", "Blood group not found in stock")

        con.close()

    ############################# Load Data Function ##############################################
    def load_data():
        for item in StockIncrease_root.tree.get_children():
            StockIncrease_root.tree.delete(item)

        con = sqlite3.connect("BloodBank.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM stock")
        rows = cursor.fetchall()
        con.close()

        for row in rows:
            StockIncrease_root.tree.insert("", tk.END, values=row)

    StockIncrease_root.tree = ttk.Treeview(
        StockIncrease_root, columns=('blood group', 'units'), show='headings')
    StockIncrease_root.tree.heading('blood group', text='Blood Group')
    StockIncrease_root.tree.heading('units', text='Units')
    StockIncrease_root.tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    load_data()

    # Frame to hold the buttons at the bottom
    button_frame = Frame(StockIncrease_root, bg="#6e1423")
    button_frame.pack(fill=X, side=BOTTOM, pady=10)

    # Update button
    update_btn = Button(button_frame, text='update', font=(
        "bold"), width=9, bg="#003049", fg="white", command=update_table)
    update_btn.pack(side=LEFT, padx=10)

    # Close button
    close_btn = Button(button_frame, text='close', font=(
        "bold"), width=9, bg="#003049", fg="white", command=StockIncrease_root.destroy)
    close_btn.pack(side=RIGHT, padx=10)

    # Start the main loop
    StockIncrease_root.mainloop()


if __name__ == "__main__":
    display_StockIncrease()
