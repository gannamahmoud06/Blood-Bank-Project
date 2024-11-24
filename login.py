from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import Home


class BloodBanking:
    #######################################################
    def center_window(self):
        w = 1350
        h = 710
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = int((screen_w - w) / 2)
        y = int((screen_h - h) / 2)
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    #######################################################
    def __init__(self, root):
        self.root = root
        self.root.title("Blood Banking")
        self.root.resizable(False, False)
        self.root["bg"] = "#6e1423"
        self.center_window()
        # ------------------show icon---------------------------------------------------
        self.root.iconphoto(True, self.get_icon())
        # ---------------------Frame for the Background---------------------------------
        self.frame2 = Frame(
            self.root, width=1350, height=710
        )
        self.frame2.place(x=0, y=0, relwidth=1, relheight=1)
        # ---------------------Show Background----------------------------------------------
        self.set_bg_label()
        # -----------------Username lbl & password lbl--------------------------------
        username = Label(
            self.root,
            text="Username",
            font=("arial", 18, "bold"),
            fg="#003049",
        )
        password = Label(
            self.root,
            text="Password",
            font=("arial", 18, "bold"),
            # bg="#6e1423",
            fg="#003049",
        )
        # -------------------verify Username & password-----------------------------

        def authenticate():
            valid_username = "admin"
            valid_password = "password"
            username = ent_user.get()
            password = ent_pass.get()

            if username == valid_username and password == valid_password:
                root.destroy()
                home_page = Home.HomeApp()
                # Create an instance of HomePage from the Home module

            elif not username or not password:
                messagebox.showerror("Error", "All fields are mandatory")

            else:
                messagebox.showerror("Error", "Invalid username or password")
        # ------------------------login Button------------------------------------
        b1 = Button(
            self.root,
            text="Login",
            relief="raised",
            font=("arial", 18, "bold"),
            bg="#003049",
            fg="white",
            width=10,
            command=authenticate,
        )
        # --------------------------Entry username&password-----------------------
        ent_user = Entry(self.root, width=18, font=("Arial", 16), bg="#f8e5ee")
        ent_pass = Entry(self.root, width=18, font=(
            "Arial", 16), bg="#f8e5ee", show="*"
        )
        # ------------------places of username&password "lbl,entry" and Login Btn----------------
        username.place(x=450, y=200)
        password.place(x=450, y=275)

        ent_user.place(x=650, y=200)
        ent_pass.place(x=650, y=275)

        b1.place(x=580, y=380)

    # ------------------icon------------------------------------
    def get_icon(self):
        img = Image.open("project pictures/enter.png")
        return ImageTk.PhotoImage(img)
    # ------------------------Background----------------------------

    def set_bg_label(self):
        bg_img = Image.open("project pictures/login3.png")

        self.frame2.bg_photo = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.frame2, image=self.frame2.bg_photo)
        bg_label.pack(side=LEFT, fill=BOTH, expand=True)


if __name__ == "__main__":
    root = Tk()
    obj = BloodBanking(root)
    root.mainloop()

