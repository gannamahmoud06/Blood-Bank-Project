import sqlite3
import tkinter as tk
from tkinter import ttk


def fetch_data(blood_group):
    conn = sqlite3.connect('bloodbank.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM doner WHERE bloodGroup LIKE ?",
                   ('%' + blood_group + '%',))
    records = cursor.fetchall()

    conn.close()

    return records


def display_SearchBloodGroup():
    def search():

        blood_group = blood_group_combo.get()

        records = fetch_data(blood_group)

        for i in table.get_children():
            table.delete(i)

        for record in records:
            table.insert('', tk.END, values=(
                record[0], record[1], record[9], record[10]))

    SearchBloodGroup_root = tk.Tk()

    ######################### Center frame ########################################
    w = 850
    h = 500
    screenW = SearchBloodGroup_root.winfo_screenwidth()
    screenh = SearchBloodGroup_root.winfo_screenheight()
    x = int((screenW - w) / 2)
    y = int((screenh - h) / 2)
    SearchBloodGroup_root.geometry(f"{w}x{h}+{x}+{y}")
    SearchBloodGroup_root.resizable(False, False)
    #################################################################

    SearchBloodGroup_root.title("Search Blood Donor (Blood Group)")
    SearchBloodGroup_root.iconbitmap("project pictures/Blood group.ico")
    SearchBloodGroup_root.configure(bg="#6e1423")

 # --------------------------Title --------------------------------------
    title_label = tk.Label(SearchBloodGroup_root, text="Search Blood Donor (Blood Group)", font=(
        "Cambria", 40, "bold", "italic"), bg="#6e1423", fg="#f8e5ee")
    title_label.pack(pady=10)

 # -------------------------- bloodgroup label--------------------------------
    address_label = tk.Label(SearchBloodGroup_root, text="Blood Group", font=(
        "arial", 18, "bold"), bg="#6e1423", fg="#f8e5ee")
    address_label.pack(pady=5)

 # ---------------------------bloodgroup entry--------------------------------
    blood_group_combo = ttk.Combobox(SearchBloodGroup_root, values=(
        "A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-" ),state="readonly", font=("Segoe UI", 14))
    blood_group_combo.pack(pady=5)

 # ---------------------------Treeview table--------------------------------
    table = ttk.Treeview(SearchBloodGroup_root, columns=(
        "ID", "Name", "City", "Address"), show='headings')
    table.heading("ID", text="ID")
    table.heading("Name", text="Name")
    table.heading("City", text="City")
    table.heading("Address", text="Address")

    table.column("ID", anchor=tk.CENTER)
    table.column("Name", anchor=tk.CENTER)
    table.column("City", anchor=tk.CENTER)
    table.column("Address", anchor=tk.CENTER)
    
    table.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    ###############################################################################################
 # ---------------------------Search button----------------------------------
    search_button = tk.Button(SearchBloodGroup_root, text="Search", font=(
        "Tahoma", 14), bg="#003049", fg="white", command=search)
    search_button.pack(side=tk.LEFT, padx=10, pady=10)
 # ---------------------------close Function("Neeeew")----------------------------------

    def CloseFun():
        SearchBloodGroup_root.destroy()
 # --------------------------- Close button-----------------------------------
    close_button = tk.Button(
        SearchBloodGroup_root,
        text="Close",
        font=("Tahoma", 14),
        command=CloseFun,
        bg="#003049",
        fg="white"
    )
    close_button.pack(side=tk.RIGHT, padx=10, pady=10)

    SearchBloodGroup_root.mainloop()


if __name__ == "__main__":
    display_SearchBloodGroup()
