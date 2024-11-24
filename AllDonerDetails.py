import tkinter as tk
from tkinter import *
from tkinter import messagebox, Menu
from tkinter import ttk
import sqlite3


def display_AllDonerDetails():
    AllDonerDetails_root = tk.Tk()
    AllDonerDetails_root.title("Doner Details")
    # ---------------------------center frame--------------------------
    w = 750
    h = 500
    screenwidth = AllDonerDetails_root.winfo_screenwidth()
    screenheight = AllDonerDetails_root.winfo_screenheight()
    x = int((screenwidth - w) / 2)
    y = int((screenheight - h) / 2)
    AllDonerDetails_root.geometry(f'{w}x{h}+{x}+{y}')
    AllDonerDetails_root.resizable(False, False)
    AllDonerDetails_root.configure(bg="#6e1423")
    # -------------------------icon--------------------------------------
    AllDonerDetails_root.iconbitmap("project pictures/Blood group.ico")
    # --------------------------lbl--------------------------------------
    lbl = Label(AllDonerDetails_root, text='All Doner (Details)', font=(
       "Cambria" , 45 , "bold" , "italic"), bg="#6e1423", fg="#f8e5ee")
    lbl.pack(pady=20)
    # -------------------------Tree of stock Details----------------------------
    frame = Frame(AllDonerDetails_root)
    frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    tree = ttk.Treeview(frame, columns=[
        "ID", "Name", "Father Name", "Mother Name", "Date Of Birth",
        "Mobile.No", "Gender", "Email", "Blood Group", "City", "Address"], show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Father Name", text="Father Name")
    tree.heading("Mother Name", text="Mother Name")
    tree.heading("Date Of Birth", text="Date Of Birth")
    tree.heading("Mobile.No", text="Mobile.No")
    tree.heading("Gender", text="Gender")
    tree.heading("Email", text="Email")
    tree.heading("Blood Group", text="Blood Group")
    tree.heading("City", text="City")
    tree.heading("Address", text="Address")
    tree.column("ID", anchor=tk.CENTER)
    tree.column("Name", anchor=tk.CENTER)
    tree.column("Father Name", anchor=tk.CENTER)
    tree.column("Mother Name", anchor=tk.CENTER)
    tree.column("Date Of Birth", anchor=tk.CENTER)
    tree.column("Mobile.No", anchor=tk.CENTER)
    tree.column("Gender", anchor=tk.CENTER)
    tree.column("Email", anchor=tk.CENTER)
    tree.column("Blood Group", anchor=tk.CENTER)
    tree.column("City", anchor=tk.CENTER)
    tree.column("Address", anchor=tk.CENTER)

    # --------------------------scrollbar--------------------------------------
    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(side=tk.RIGHT, fill=tk.Y)

    hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(side=tk.BOTTOM, fill=tk.X)

    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # ---------------------- Close button------------------------------------------------------
    close_btn = Button(AllDonerDetails_root, text='Close', font=("bold"), width=9, bg="#003049",
                       fg="white", command=AllDonerDetails_root.destroy)
    close_btn.pack(side=tk.RIGHT, padx=10, pady=10)
    # --------------------------print fun------------------------------------------------------

    def Printfun():
        for item in tree.get_children():
            tree.delete(item)
        con = sqlite3.connect("BloodBank.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM doner")
        rows = cursor.fetchall()
        con.close()

        for row in rows:
            tree.insert("", tk.END, values=row)
    # -------------------------Print Button----------------------------------------------------
    btnprint = tk.Button(AllDonerDetails_root, text="Print", font=("bold"), width=9, bg="#003049",
                         fg="white", command=Printfun)
    btnprint.pack(side=tk.LEFT, padx=10, pady=10)
    AllDonerDetails_root.mainloop()

if __name__ == "__main__":
    display_AllDonerDetails()
