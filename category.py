from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("TITE Stock Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        ############ Variables ###############
        self.var_cat_id = StringVar()
        self.var_name = StringVar()

        ############### Title ################
        lbl_title = Label(self.root, text="Manage Product Category", font=("times new roman", 30), bg="#A52A2A", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X, pady=20, padx=10)
        lbl_name = Label(self.root, text="Enter Category Name: ", font=("times new roman", 25), bg="white").place(x=50, y=100)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("times new roman", 18), bg="lightyellow").place(x=50, y=150, width=300)

        # Buttons
        btn_add = Button(self.root, text="ADD", command=self.add, font=("times new roman", 18, "bold"), bg="#301934", fg="white", cursor="hand2").place(x=360, y=150, height=30, width=100)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("times new roman", 18, "bold"), bg="#FFA500", fg="white", cursor="hand2").place(x=470, y=150, height=30, width=100)

        # Category Details
        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=653, y=90, width=420, height=90)

        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)

        self.CategoryTable = ttk.Treeview(cat_frame, columns=("cid", "name"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)

        self.CategoryTable.heading("cid", text="C ID")
        self.CategoryTable.heading("name", text="NAME")
        self.CategoryTable["show"] = "headings"

        self.CategoryTable.column("cid", width=90)
        self.CategoryTable.column("name", width=100)
        self.CategoryTable.pack(fill=BOTH, expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>", self.get_data)

        ########## Images ##########

        self.im1 = Image.open("Images/cat.jpg")
        self.im1 = self.im1.resize((500, 250), Image.Resampling.LANCZOS)
        self.im1 = ImageTk.PhotoImage(self.im1)

        self.lbl_im1 = Label(self.root, image=self.im1, bd=2, relief=RAISED)
        self.lbl_im1.place(x=50, y=210)

        self.im2 = Image.open("Images/category.jpg")
        self.im2 = self.im2.resize((500, 250), Image.Resampling.LANCZOS)        
        self.im2 = ImageTk.PhotoImage(self.im2)

        self.lbl_im2 = Label(self.root, image=self.im2, bd=2, relief=RAISED)
        self.lbl_im2.place(x=575, y=210)

        self.show()

    ######################### add ##############################################
    def add(self):
        con = sqlite3.connect(database=r'sms.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Category name must be required", parent=self.root)

            else:
                cur.execute("Select * from category where name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Category already present, try different", parent=self.root)
                else:
                    cur.execute("Insert into category (name) values(?)", (self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)
                    self.show()  # Refresh the data after adding
                    self.var_name.set("")  # Clear input field after adding

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'sms.db')
        cur = con.cursor()
        try:
            cur.execute("select * from category")
            rows = cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.CategoryTable.focus()
        content = (self.CategoryTable.item(f))
        row = content['values']
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    ################# DELETE ####################
    def delete(self):
        con = sqlite3.connect(database=r'sms.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Error", "Please select category from the list", parent=self.root)

            else:
                cur.execute("Select * from category where cid=?", (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Not available, Try again!!", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from category where cid=?", (self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Category Deleted Successfully", parent=self.root)
                        self.show()  # Refresh the data after deleting
                        self.var_cat_id.set("")  # Clear selected ID
                        self.var_name.set("")  # Clear input field
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
