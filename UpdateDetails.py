import tkinter as tk
from tkinter import *
from tkinter import messagebox, Menu
from tkinter import ttk
import sqlite3


def display_UpdateDetails():
    Update_root = tk.Tk()
    
    #######################Center Frame###############################
    w = 750
    h = 500
    screenW = Update_root.winfo_screenwidth()
    screenh = Update_root.winfo_screenheight()
    x = int((screenW - w) / 2)
    y = int((screenh - h) / 2)
    Update_root.geometry(f"{w}x{h}+{x}+{y}")
    Update_root.resizable(False, False) 

    
    Update_root.title("Update Page")
    Update_root["bg"] = "#6e1423"
    Update_root.iconbitmap("project pictures/Blood group.ico")
    
    font = ("arial" , 18 , "bold") 

    lblUpdate = tk.Label(Update_root , text="Update" , font = ("Cambria" , 45 , "bold" , "italic")  , bg ="#6e1423" , fg = "#f8e5ee" )
    lblUpdate.pack()
    ############################## Doner ID ##########################
    lblDonerID = tk.Label(Update_root , text = "Doner ID" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblDonerID.place(x = 200 , y = 90)
    ############################## IDs in database ##########################
    conn = sqlite3.connect('BloodBank.db')
    cur = conn.cursor()

    cur.execute("SELECT DonerID FROM doner")
    
    records = cur.fetchall()

    conn.close()

    ###############################################################################
    entDonerID = ttk.Combobox(Update_root , values= records)
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
    btnSearch = tk.Button(Update_root ,text="Search" , width= 20  , bg="#003049",
    fg="white" , command= SearchFun)
    btnSearch.place(x=485,y=95)  
        
    ############################### Full Name #######################################
    lblFullName = tk.Label(Update_root , text = "Full Name" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblFullName.place(x = 10 , y = 170)
    entFullName = tk.Entry(Update_root)
    entFullName.place(x =175 , y = 180)
    
    ############################# Father Name ############################################
    lblFatherName = tk.Label(Update_root , text = "Father Name" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblFatherName.place(x = 10 , y = 215)
    entFatherName = tk.Entry(Update_root)
    entFatherName.place(x =175 , y = 225)
    
    ############################### Mother Name ###########################################
    lblMotherName = tk.Label(Update_root , text = "Mother Name" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblMotherName.place(x = 10 , y = 260)
    entMotherName = tk.Entry(Update_root)
    entMotherName.place(x =175 , y = 270)
    
    ############################### DOB #################################################
    lblDOB = tk.Label(Update_root , text = "Date Of Birth" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblDOB.place(x = 10 , y = 305)
    entDOB = tk.Entry(Update_root)
    entDOB.place(x =175 , y = 315)
    
    ################################### Mobile Number ########################################
    lblMobileNo = tk.Label(Update_root , text = "Mobile.No" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblMobileNo.place(x = 10 , y = 350)
    entMobileNo = tk.Entry(Update_root)
    entMobileNo.place(x =175 , y = 360)
    
    ##################################### Gender #####################################3
    
    lblSex = tk.Label(Update_root , text = "Gender" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblSex.place(x = 435 , y = 170)
    entSex = ttk.Combobox(Update_root,values=["Male", "Female"],
    height=5,
    width=17,
    state="readonly")
    entSex.place(x =600 , y = 180)
    
    ########################################### Email ###################################3
    lblEmail = tk.Label(Update_root , text = "Email" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblEmail.place(x = 435 , y = 215)
    entEmail = tk.Entry(Update_root)
    entEmail.place(x =600 , y = 225)
    
    ########################################### Blood Group ##############################
    
    lblBG = tk.Label(Update_root , text = "Blood Group" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblBG.place(x = 435 , y = 260)
    entBG = ttk.Combobox(Update_root,height=5,
    width=17,
    values=["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"],
    state="readonly")
    entBG.place(x =600 , y = 270)
    
    ################################## City ############################################3
    lblCity = tk.Label(Update_root , text = "City" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblCity.place(x = 435 , y = 305)
    entCity = tk.Entry(Update_root)
    entCity.place(x =600 , y = 315)
    
    
    ############################################## Address ##################################
    lblAddr = tk.Label(Update_root , text = "Address" , font = font , bg ="#6e1423" , fg = "#f8e5ee")
    lblAddr.place(x = 435 , y = 350)
    entAddr = tk.Entry(Update_root)
    entAddr.place(x =600 , y = 360)
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
        Update_root.destroy()
    ########################################## Update Function #################################
    def UpdateFun():
        ID = entDonerID.get()
        if ID:
            fullName = entFullName.get()
            fatherName = entFatherName.get()
            motherName = entMotherName.get()
            dob = entDOB.get()
            mobileNo = entMobileNo.get()
            sex = entSex.get()
            email = entEmail.get()
            bloodGroup = entBG.get()
            city = entCity.get()
            address = entAddr.get()

            conn = sqlite3.connect("BloodBank.db")
            cur = conn.cursor()
            cur.execute("""
                UPDATE doner SET
                Name = ?,
                FatherName = ?,
                MotherName = ?,
                DOB = ?,
                MobileNo = ?,
                Gender = ?,
                Email = ?,
                BloodGroup = ?,
                City = ?,
                Address = ?
                WHERE DonerID = ?
            """, (fullName, fatherName, motherName, dob, mobileNo, sex, email, bloodGroup, city, address, ID))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success", "Record updated successfully")
    ########################################## buttons #########################################
    btnUpdate = tk.Button(Update_root,text = "Update" ,font = ("bold"), width= 9 , bg="#003049",
    fg="white" , command=UpdateFun)
    btnUpdate.place(x= 90 , y = 450)

    btnReset = tk.Button(Update_root,text = "Reset" , font = ("bold"),width= 9 , bg="#003049",
    fg="white" , command=ResetFun)
    btnReset.place(x= 300 , y = 450)
    
    btnClose = tk.Button(Update_root,text = "Close" , font = ("bold"),width= 9 ,bg="#003049",
    fg="white" , command=CloseFun)
    btnClose.place(x= 510 , y = 450)
    
    Update_root.mainloop()

if __name__ == "__main__":
    display_UpdateDetails()