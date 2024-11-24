import tkinter as tk
from tkinter import *
from tkinter import messagebox, Menu
from tkinter import ttk
import sqlite3


def display_Delete():
    Delete_root = tk.Tk()
    
    ####################### Center Frame ###############################
    w = 750
    h = 500
    screenW = Delete_root.winfo_screenwidth()
    screenh = Delete_root.winfo_screenheight()
    x = int((screenW - w) / 2)
    y = int((screenh - h) / 2)
    Delete_root.geometry(f"{w}x{h}+{x}+{y}")
    Delete_root.resizable(False, False)

    
    Delete_root.title("Delete Page")
    Delete_root["bg"] = "#6e1423"
    Delete_root.iconbitmap("project pictures/Blood group.ico")
    
    font = ("arial" , 18 , "bold") 

    lblDelete = tk.Label(Delete_root , text="Delete Doner" , font = ("Cambria" , 45 , "bold" , "italic")  , bg ="#6e1423" , fg = "#f8e5ee" )
    lblDelete.pack()
    
    ############################## Doner ID ##########################
    lblDonerID = tk.Label(Delete_root , text = "Doner ID" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblDonerID.place(x = 200 , y = 90)
    ############################## IDs in database ##########################
    conn = sqlite3.connect('BloodBank.db')
    cur = conn.cursor()

    cur.execute("SELECT DonerID FROM doner")
    
    records = cur.fetchall()

    conn.close()

    ###############################################################################
    entDonerID = ttk.Combobox(Delete_root , values= records)
    entDonerID.place(x = 320 , y = 97)
        
    
    ########################Search Function####################################
    def SearchFun():
        ID = entDonerID.get()
        if ID :
            conn = sqlite3.connect("BloodBank.db")
            cur = conn.cursor()
            cur.execute("SELECT * from doner where DonerID = ?" , (ID,))
            raw = cur.fetchone()
            if raw:
                entFullName.delete(0,tk.END)
                entFatherName.delete(0,tk.END)
                entMotherName.delete(0,tk.END)
                entMobileNo.delete(0,tk.END)
                entCity.delete(0,tk.END)
                entAddr.delete(0,tk.END)
                entBG.delete(0,tk.END)
                entDOB.delete(0,tk.END)
                entEmail.delete(0,tk.END)
                entSex.delete(0,tk.END)
            
                entFullName.insert(0,raw[1])
                entFatherName.insert(0,raw[2])
                entMotherName.insert(0,raw[3])
                entMobileNo.insert(0,raw[5])
                entCity.insert(0,raw[9])
                entAddr.insert(0,raw[10])
                entBG.set(raw[8])
                entDOB.insert(0,raw[4])
                entEmail.insert(0,raw[7])
                entSex.set(raw[6])
            else:
                entFullName.delete(0,tk.END)
                entFatherName.delete(0,tk.END)
                entMotherName.delete(0,tk.END)
                entMobileNo.delete(0,tk.END)
                entCity.delete(0,tk.END)
                entAddr.delete(0,tk.END)
                entBG.delete(0,tk.END)
                entDOB.delete(0,tk.END)
                entEmail.delete(0,tk.END)
                entSex.delete(0,tk.END)
                        
                tk.messagebox.showerror("Error", "Donor ID does not exist")
            conn.close()

    ############################### Search Button ###################################
    btnSearch = tk.Button(Delete_root ,text="Search" , width= 20  , bg="#003049",
    fg="white" , command= SearchFun)
    btnSearch.place(x=485,y=95)
    
    ############################### Full Name #######################################
    lblFullName = tk.Label(Delete_root , text = "Full Name" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblFullName.place(x = 10 , y = 170)
    entFullName = tk.Entry(Delete_root)
    entFullName.place(x =175 , y = 180)
    
    ############################# Father Name ############################################
    lblFatherName = tk.Label(Delete_root , text = "Father Name" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblFatherName.place(x = 10 , y = 215)
    entFatherName = tk.Entry(Delete_root)
    entFatherName.place(x =175 , y = 225)
    
    ############################### Mother Name ###########################################
    lblMotherName = tk.Label(Delete_root , text = "Mother Name" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblMotherName.place(x = 10 , y = 260)
    entMotherName = tk.Entry(Delete_root)
    entMotherName.place(x =175 , y = 270)
    
    ############################### DOB #################################################
    lblDOB = tk.Label(Delete_root , text = "Date Of Birth" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblDOB.place(x = 10 , y = 305)
    entDOB = tk.Entry(Delete_root)
    entDOB.place(x =175 , y = 315)
    
    ################################### Mobile Number ########################################
    lblMobileNo = tk.Label(Delete_root , text = "Mobile.No" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblMobileNo.place(x = 10 , y = 350)
    entMobileNo = tk.Entry(Delete_root)
    entMobileNo.place(x =175 , y = 360)
    
    ##################################### Gender #####################################3
    lblSex = tk.Label(Delete_root , text = "Gender" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblSex.place(x = 435 , y = 170)
    entSex = ttk.Combobox(Delete_root,values=["Male", "Female"],
    height=5,
    width=17,
    state="readonly")
    entSex.place(x =600 , y = 180)
    
    ########################################### Email ###################################3
    lblEmail = tk.Label(Delete_root , text = "Email" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblEmail.place(x = 435 , y = 215)
    entEmail = tk.Entry(Delete_root)
    entEmail.place(x =600 , y = 225)
    
    ########################################### Blood Group ##############################
    lblBG = tk.Label(Delete_root , text = "Blood Group" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblBG.place(x = 435 , y = 260)
    entBG = ttk.Combobox(Delete_root,height=5,
    width=17,
    values=["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"],
    state="readonly")
    entBG.place(x =600 , y = 270)
    
    ################################## City ############################################3
    lblCity = tk.Label(Delete_root , text = "City" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblCity.place(x = 435 , y = 305)
    entCity = tk.Entry(Delete_root)
    entCity.place(x =600 , y = 315)
    
    
    ############################################## Address ##################################
    lblAddr = tk.Label(Delete_root , text = "Address" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblAddr.place(x = 435 , y = 350)
    entAddr = tk.Entry(Delete_root)
    entAddr.place(x =600 , y = 360)
    ########################################## Delete Function #################################
    def DeleteFun():
        ID = entDonerID.get()
        conn = sqlite3.connect("BloodBank.db")  # Update with your database path
        cur = conn.cursor()
        if ID:
            cur.execute("DELETE FROM doner WHERE DonerID = ?", (ID,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Successfully Deleted")
            ResetFun()
        else:
            tk.messagebox.showerror("Error", "Donor ID does not exist")
    ################################# Reset Function ###########################################
    def ResetFun():
        entDonerID.delete(0 , tk.END)
        entFullName.delete(0,tk.END)
        entFatherName.delete(0,tk.END)
        entMotherName.delete(0,tk.END)
        entMobileNo.delete(0,tk.END)
        entCity.delete(0,tk.END)
        entAddr.delete(0,tk.END)
        entBG.set("")
        entDOB.delete(0,tk.END)
        entEmail.delete(0,tk.END)
        entSex.set("")
        
        entDonerID.config(state=tk.NORMAL)
    ###################################### Delete Function ######################################
    def CloseFun():
        Delete_root.destroy()
    ########################################## buttons #########################################
    btnDelete = tk.Button(Delete_root,text = "Delete" ,font = ("bold"), width= 9 , bg="#003049",
    fg="white" , command= DeleteFun)
    btnDelete.place(x= 90 , y = 450)

    btnReset = tk.Button(Delete_root,text = "Reset" , font = ("bold"),width= 9 , bg="#003049",
    fg="white" , command=ResetFun)
    btnReset.place(x= 300 , y = 450)
    
    btnClose = tk.Button(Delete_root,text = "Close" , font = ("bold"),width= 9 ,bg="#003049",
    fg="white" , command=CloseFun)
    btnClose.place(x= 510 , y = 450)
    
    Delete_root.mainloop()

if __name__ == "__main__":
    display_Delete()