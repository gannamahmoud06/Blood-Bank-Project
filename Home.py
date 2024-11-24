import tkinter as tk
from tkinter import *
from tkinter import messagebox, Menu
from tkinter import ttk
from PIL import ImageTk, Image
import Delete
import AddNewDoner
import UpdateDetails
import StockIncrease
import StockDetails
import SearchLocation
import SearchBloodGroup
import AllDonerDetails
import StockDecrease
from login import BloodBanking


def HomeApp():
    root = tk.Tk()

    root.title("Home")
    
    w = 1350
    h = 710

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    y = int(screen_height / 2 - h / 2)
    x = int(screen_width / 2 - w / 2)

    root.geometry(f"{w}x{h}+{x}+{y}")    
    root.resizable(False, False)
    # ---------------------------icon--------------------------------------
    img = Image.open("project pictures/Blood group.png")
    ico = ImageTk.PhotoImage(img)
    root.iconphoto(False, ico)
    # ----------------------Background-------------------------------------
    bg_img = ImageTk.PhotoImage(
        Image.open("project pictures/home.png"))

    bg_label = Label(root, image=bg_img)
    bg_label.pack(side=LEFT, fill=BOTH, expand=True)
    # -----------------Functions Of the Menu list-------------------------

    def add_new_donor():
        # Placeholder for Add New Donor window

        add_new_donor_page = AddNewDoner.display_AddNewDoner()

    def update_donor_details():

        update_donor_details_page = UpdateDetails.display_UpdateDetails()

    def all_donor_details():

        all_donor_details_page = AllDonerDetails.display_AllDonerDetails()

    def search_location():

        search_location_page = SearchLocation.display_SearchLocation()

    def search_blood_group():

        search_blood_group_page = SearchBloodGroup.display_SearchBloodGroup()

    def stock_increase():

        stock_increase_page = StockIncrease.display_StockIncrease()

    def stock_decrease():

        stock_decrease_page = StockDecrease.display_StockDecrease()

    def stock_details():

        stock_details_page = StockDetails.display_StockDetails()

    def delete_donor():

        delete_donor_page = Delete.display_Delete()

    def logout():
        root.destroy()
        new_root = Tk()
        login_page = BloodBanking(new_root)
        # Close the current window

    def exit_app():
        if messagebox.askyesno("Exit", "Do you really want to close the Application?"):
            root.destroy()  # Close the application

    # ----------------------Create the menu bar--------------------------
    menu_bar = tk.Menu(root)
    root.configure(menu=menu_bar)
    # ----------------------Donor Menu----------------------------------
    donor_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Donor", menu=donor_menu)
    donor_menu.add_command(label="Add New", command=add_new_donor)
    donor_menu.add_command(
        label="Update Details", command=update_donor_details
    )
    donor_menu.add_command(
        label="All Donor Details", command=all_donor_details
    )

    # -------------------Search Blood Donor Menu-----------------------
    search_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Search Blood Donor", menu=search_menu)
    search_menu.add_command(label="Location", command=search_location)
    search_menu.add_command(label="Blood Group", command=search_blood_group)

    # -------------------Stock Menu-----------------------------------
    stock_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Stock", menu=stock_menu)
    stock_menu.add_command(label="Increase", command=stock_increase)
    stock_menu.add_command(label="Decrease", command=stock_decrease)
    stock_menu.add_command(label="Details", command=stock_details)

    # ----------------Delete Donor Menu-----------------------------
    delete_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Delete Donor", menu=delete_menu)
    delete_menu.add_command(label="Delete Donor", command=delete_donor)

    # ----------------Exit Menu-------------------------------------
    exit_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Exit", menu=exit_menu)
    exit_menu.add_command(label="Logout", command=logout)
    exit_menu.add_command(label="Exit", command=exit_app)

    root.mainloop()


if __name__ == "__main__":
    HomeApp()
