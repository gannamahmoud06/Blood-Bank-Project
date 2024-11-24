import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox, Menu
from tkinter import ttk
import Home


def display_StockDetails():
    StockDetails_root = tk.Tk()
    StockDetails_root.title("Stock Details")
    # ---------------------------center frame--------------------------
    w = 750
    h = 500
    screenwidth = StockDetails_root.winfo_screenwidth()
    screenheight = StockDetails_root.winfo_screenheight()
    x = int((screenwidth - w) / 2)
    y = int((screenheight - h) / 2)
    StockDetails_root.geometry(f"{w}x{h}+{x}+{y}")
    StockDetails_root.resizable(False, False)
    StockDetails_root.configure(bg="#6e1423")
    # -------------------------icon--------------------------------------
    StockDetails_root.iconbitmap("project pictures/Blood group.ico")
    # --------------------------lbl--------------------------------------
    lbl = Label(
        StockDetails_root,
        text="Stock (Details)",
        font=("Cambria" , 45 , "bold" , "italic"),
        bg="#6e1423",
        fg="#f8e5ee",
    )
    lbl.pack(pady=20)
    # -------------------------Frame for Treeview and Scrollbars----------------------------
    frame = Frame(StockDetails_root)
    frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # -------------------------Tree of Stock Details----------------------------
    tree = ttk.Treeview(frame, columns=["blood group", "units"], show="headings")
    tree.heading("blood group", text="Blood Group")
    tree.heading("units", text="Units")
    tree.column("blood group", anchor=tk.CENTER)
    tree.column("units", anchor=tk.CENTER)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    # --------------------------Vertical Scrollbar-------------------------------------
    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(side=tk.RIGHT, fill=tk.Y)

    # ---------------------- Close button------------------------------------
    close_btn = Button(
        StockDetails_root,
        text="Close",
        font=("bold"),
        width=9,
        bg="#003049",
        fg="white",
        command=StockDetails_root.destroy,
    )
    close_btn.pack(side=tk.RIGHT, padx=10, pady=10)

    # --------------------------print fun--------------------------------------

    def Printfun():
        for item in tree.get_children():
            tree.delete(item)
        con = sqlite3.connect("BloodBank.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM stock")
        rows = cursor.fetchall()
        con.close()

        for row in rows:
            tree.insert("", tk.END, values=row)

    # -------------------------Print Button--------------------------
    btnprint = tk.Button(
        StockDetails_root,
        text="Print",
        font=("bold"),
        width=9,
        bg="#003049",
        fg="white",
        command=Printfun,
    )
    btnprint.pack(side=tk.LEFT, padx=10, pady=10)

    StockDetails_root.mainloop()
if __name__ == "__main__":
    display_StockDetails()
