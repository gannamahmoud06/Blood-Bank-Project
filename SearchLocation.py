import sqlite3
import tkinter as tk
from tkinter import ttk

def fetch_data(address):
    conn = sqlite3.connect("bloodbank.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM doner WHERE address LIKE ?",
                   ("%" + address + "%",))
    records = cursor.fetchall()
    conn.close()

    return records


def display_SearchLocation():
    def search():

        address = address_entry.get()

        records = fetch_data(address)

        for i in table.get_children():
            table.delete(i)

        for record in records:
            table.insert('', tk.END, values=(
                record[0], record[1], record[9], record[10]))

    SearchLocation_root = tk.Tk()
    ######################### center frame ########################################
    w = 850
    h = 500
    screenW = SearchLocation_root.winfo_screenwidth()
    screenh = SearchLocation_root.winfo_screenheight()
    x = int((screenW - w) / 2)
    y = int((screenh - h) / 2)
    SearchLocation_root.geometry(f"{w}x{h}+{x}+{y}")
    SearchLocation_root.resizable(False, False)
    ###################################################
    SearchLocation_root.title("Search Blood Donor (Address)")
    SearchLocation_root.iconbitmap("project pictures/Blood group.ico")
    SearchLocation_root.configure(bg="#6e1423")

    # --------------------------Title --------------------------------------
    title_label = tk.Label(
        SearchLocation_root,
        text="Search Blood Donor (Address)",
        font=("Cambria", 40, "bold", "italic"),
        bg="#6e1423",
        fg="#f8e5ee",
    )
    title_label.pack(pady=10)

    # -------------------------- Address label--------------------------------
    address_label = tk.Label(
        SearchLocation_root,
        text="Address",
        font=("arial", 18, "bold"),
        bg="#6e1423",
        fg="#f8e5ee",
    )
    address_label.pack(pady=5)

    # ---------------------------Address entry--------------------------------
    address_entry = tk.Entry(SearchLocation_root, font=("Tahoma", 14))
    address_entry.pack(pady=5, padx=10, fill=tk.X)

    # ---------------------------Treeview table--------------------------------
    table = ttk.Treeview(
        SearchLocation_root, columns=("ID", "Name", "City", "Address"), show="headings"
    )
    table.heading("ID", text="ID")
    table.heading("Name", text="Name")
    table.heading("City", text="City")
    table.heading("Address", text="Address")

    table.column("ID", anchor=tk.CENTER)
    table.column("Name", anchor=tk.CENTER)
    table.column("City", anchor=tk.CENTER)
    table.column("Address", anchor=tk.CENTER)
    # 3
    table.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # ---------------------------Search button----------------------------------
    search_button = tk.Button(
        SearchLocation_root,
        text="Search",
        font=("Tahoma", 14),
        bg="#003049",
        fg="white",
        command=search,
    )
    search_button.pack(side=tk.LEFT, padx=10, pady=10)
    # ----------------------------close Function("Neeeeeew")----------------------------------

    def CloseFun():
        SearchLocation_root.destroy()
    # --------------------------- Close button-----------------------------------
    close_button = tk.Button(
        SearchLocation_root,
        text="Close",
        font=("Tahoma", 14),
        command=CloseFun,
        bg="#003049",
        fg="white",
    )
    close_button.pack(side=tk.RIGHT, padx=10, pady=10)

    SearchLocation_root.mainloop()


if __name__ == "__main__":
    display_SearchLocation()
