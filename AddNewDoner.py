import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3


def display_AddNewDoner():
    ######################################3 Center frame ###################################
    AddNewDone_root = tk.Tk()

    w = 750
    h = 500
    screenW = AddNewDone_root.winfo_screenwidth()
    screenh = AddNewDone_root.winfo_screenheight()
    x = int((screenW - w) / 2)
    y = int((screenh - h) / 2)
    AddNewDone_root.geometry(f"{w}x{h}+{x}+{y}")
    AddNewDone_root.resizable(False, False)
    ############################ create AddNewDone_root ######################################

    AddNewDone_root.title("Add New Doner")
    AddNewDone_root.iconbitmap("project pictures/Blood group.ico")
    AddNewDone_root.config(bg="#6e1423")

    font = ("arial", 18, "bold")

    ######################################## Titel ##############################################
    lbl = tk.Label(
        AddNewDone_root,
        text="Add New Doner",
        font=("Cambria", 45, "bold", "italic"),
        bg="#6e1423",
        fg="#f8e5ee",
    )
    lbl.place(x = 175 , y = 40)
    ####################################3 name ############################################
    name_lbl = tk.Label(
        AddNewDone_root, text="Full Name", fg="#f8e5ee", bg="#6e1423", font=font
    )
    name_lbl.place(x=10, y=170)
    name_ent = tk.Entry(AddNewDone_root)
    name_ent.place(x=175, y=180)
    ######################################3 father name #############################################
    father_lbl = tk.Label(
        AddNewDone_root, text="Father Name", font=font, bg="#6e1423", fg="#f8e5ee"
    )
    father_lbl.place(x=10, y=215)
    father_ent = tk.Entry(AddNewDone_root)
    father_ent.place(x=175, y=225)
    #######################################3 mother name ######################################3
    mother_lbl = tk.Label(
        AddNewDone_root, text="Mother Name", font=font, bg="#6e1423", fg="#f8e5ee"
    )
    mother_lbl.place(x=10, y=260)
    mother_ent = tk.Entry(AddNewDone_root)
    mother_ent.place(x=175, y=270)
    ########################################## DOB ######################################
    date_lbl = tk.Label(
        AddNewDone_root, text="Date of Birth", font=font, bg="#6e1423", fg="#f8e5ee"
    )
    date_lbl.place(x=10, y=305)
    date_ent = tk.Entry(AddNewDone_root)
    date_ent.place(x=175, y=315)
    ##################################33 mobile #############################################
    mobile_lbl = tk.Label(
        AddNewDone_root, text="Mobile No", font=font, bg="#6e1423", fg="#f8e5ee"
    )
    mobile_lbl.place(x=10, y=350)
    mobile_ent = tk.Entry(AddNewDone_root)
    mobile_ent.place(x=175, y=360)
    ####################################3 gender #############################################3
    gender_lbl = tk.Label(
        AddNewDone_root, text="Gender", font=font, bg="#6e1423", fg="#f8e5ee"
    )
    gender_lbl.place(x=435, y=170)
    gender_ent = ttk.Combobox(
        AddNewDone_root,
        # font=font,
        values=["Male", "Female"],
        height=5,
        width=17,
        state="readonly",
    )
    gender_ent.place(x=600, y=180)
    ################################### mail ###########################################
    mail_lbl = tk.Label(
        AddNewDone_root, text="E-mail", font=font, bg="#6e1423", fg="#f8e5ee"
    )
    mail_lbl.place(x=435, y=215)
    mail_ent = tk.Entry(AddNewDone_root)
    mail_ent.place(x=600, y=225)
    ##################################### BG ###########################################
    blood_lbl = tk.Label(
        AddNewDone_root, text="Blood Group", font=font, bg="#6e1423", fg="#f8e5ee"
    )
    blood_lbl.place(x=435, y=260)
    blood = ttk.Combobox(
        AddNewDone_root,
        # font=font,
        height=5,
        width=17,
        values=["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"],
        state="readonly",
    )
    blood.place(x=600, y=270)
    ##################################### city ############################################
    city_lbl = tk.Label(
        AddNewDone_root, text="City", font=font, bg="#6e1423", fg="#f8e5ee"
    )
    city_lbl.place(x=435, y=305)
    city_ent = tk.Entry(AddNewDone_root)
    city_ent.place(x=600, y=315)
    ########################################### addr ###########################################
    address_lbl = tk.Label(
        AddNewDone_root, text="Address", font=font, bg="#6e1423", fg="#f8e5ee"
    )
    address_lbl.place(x=435, y=350)
    address_txt = tk.Entry(AddNewDone_root)
    address_txt.place(x=600, y=360)

    ############################################ Functions ########################################
    def save_doner():
        full_name = str(name_ent.get())
        father_name = str(father_ent.get())
        mother_name = str(mother_ent.get())
        date_birth = str(date_ent.get())
        mobile = str(mobile_ent.get())
        gender = str(gender_ent.get())
        mail = str(mail_ent.get())
        blood_g = str(blood.get())
        city = str(city_ent.get())
        address = str(address_txt.get())
        
        
        conn = sqlite3.connect("BloodBank.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO doner (name , FatherName , MotherName , dob , MobileNo , Gender , Email , BloodGroup , city , Address) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(full_name , father_name , mother_name , date_birth , mobile , gender , mail , blood_g , city , address,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Successfully Added")
        reset_form()

    def reset_form():
        name_ent.delete(0, tk.END)
        father_ent.delete(0, tk.END)
        mother_ent.delete(0, tk.END)
        date_ent.delete(0, tk.END)
        mobile_ent.delete(0, tk.END)
        gender_ent.set("")
        mail_ent.delete(0, tk.END)
        blood.set("")
        city_ent.delete(0, tk.END)
        address_txt.delete(0, tk.END)

    def close_form():
        AddNewDone_root.destroy()

    ############################################ buttons ##########################################
    # save
    btn1 = tk.Button(
        AddNewDone_root,
        text="Save",
        font=("bold"),
        width=9,
        bg="#003049",
        fg="white",
        command=save_doner,
    )
    btn1.place(x=90, y=450)
    # reset
    btn2 = tk.Button(
        AddNewDone_root,
        text="Reset",
        font=("bold"),
        width=9,
        bg="#003049",
        fg="white",
        command=reset_form,
    )
    btn2.place(x=300, y=450)
    # close
    btn3 = tk.Button(
        AddNewDone_root,
        text="Close",
        font=("bold"),
        width=9,
        bg="#003049",
        fg="white",
        command=close_form,
    )
    btn3.place(x=510, y=450)

    AddNewDone_root.mainloop()


if __name__ == "__main__":
    display_AddNewDoner()
