from tkinter import *
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from datetime import datetime  # Import datetime module
from tkinter import messagebox

class SMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("TITE Stock Management System")
        self.root.config(bg="white")
        
        # Title
        self.icon_title = PhotoImage(file="Images/logo1.png")
        title = Label(self.root, text="TITE Stock Management System", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#ff0000", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # Logout Button
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 20, "bold"),
                            bg="#000080", fg="white", cursor="hand2", command=self.logout)
        btn_logout.place(x=1150, y=10, height=50, width=150)
       
        # Clock
        self.lbl_clock = Label(self.root, font=("times new roman", 15), bg="#000080", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        self.update_clock()  # Call the update_clock method
        
        # Left Menu
        self.MenuLogo = Image.open("Images/menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.Resampling.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)
        
        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)
        
        self.icon_side = PhotoImage(file="Images/side.png")
        
        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20, "bold"),
                         bg="#000080", fg="white").pack(side=TOP, fill=X)
        btn_employee = Button(LeftMenu, text="Employee", command=self.employee, image=self.icon_side, compound=LEFT,
                              padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_employee.pack(side=TOP, fill=X)
        btn_supplier = Button(LeftMenu, text="Supplier", command=self.supplier, image=self.icon_side, compound=LEFT,
                              padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_supplier.pack(side=TOP, fill=X)
        btn_category = Button(LeftMenu, text="Category", command=self.category, image=self.icon_side, compound=LEFT,
                              padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_category.pack(side=TOP, fill=X)
        btn_product = Button(LeftMenu, text="Product", command=self.product, image=self.icon_side, compound=LEFT,
                             padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_product.pack(side=TOP, fill=X)
        btn_sales = Button(LeftMenu, text="Sales", command=self.sales, image=self.icon_side, compound=LEFT,
                           padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_sales.pack(side=TOP, fill=X)
        btn_exit = Button(LeftMenu, text="Exit", command=self.exit_app, image=self.icon_side, compound=LEFT,
                          padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_exit.pack(side=TOP, fill=X)
        
        # Content
        self.lbl_employee = Label(self.root, text="Total Employee\n[0]", bd=5, relief=RIDGE,
                                  bg="#87CEEB", fg="#000080", font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)
        
        self.lbl_supplier = Label(self.root, text="Total Supplier\n[0]", bd=5, relief=RIDGE,
                                  bg="#87CEEB", fg="#000080", font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)
        
        self.lbl_category = Label(self.root, text="Total Category\n[0]", bd=5, relief=RIDGE,
                                  bg="#87CEEB", fg="#000080", font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)
        
        self.lbl_product = Label(self.root, text="Total Product\n[0]", bd=5, relief=RIDGE,
                                 bg="#87CEEB", fg="#000080", font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150, width=300)
        
        self.lbl_sales = Label(self.root, text="Total Sales\n[0]", bd=5, relief=RIDGE,
                               bg="#87CEEB", fg="#000080", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)
        
        self.lbl_developer = Label(self.root, text="Developer\n[0]", bd=5, relief=RIDGE,
                                   bg="#87CEEB", fg="#000080", font=("goudy old style", 20, "bold"))
        self.lbl_developer.place(x=1000, y=300, height=150, width=300)

        # Add Employee button (only visible to admin, but for now always visible)
        btn_add_emp = Button(self.root, text='Add Employee', font=("times new roman", 16, "bold"), bg="#4caf50", fg="white", command=self.add_employee_window)
        btn_add_emp.place(x=1100, y=500, width=180, height=50)
        
        # Footer
        lbl_footer = Label(self.root, text="SMS-Stock Management System | Developed By: Pankaj Kumar\nIf You are facing any type of technical error then contact us! - Email-mackystech@gmail.com; Mobile: +91-82359-10315",
                           font=("times new roman", 12), bg="#000080", fg="white")
        lbl_footer.pack(side=BOTTOM, fill=X)

        self.update_dashboard_counts()  # Start real-time dashboard updates
    
    def update_clock(self):
        now = datetime.now()
        date_time = now.strftime("Date: %d-%m-%Y   Time: %H:%M:%S")
        self.lbl_clock.config(text=f"Welcome to Stock Management System\t\t{date_time}")
        self.root.after(1000, self.update_clock)  # Update clock every 1 second
    
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)
        
    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)
    
    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)
    
    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)
    
    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)
    
    def exit_app(self):
        self.root.destroy()

    def update_dashboard_counts(self):
        import sqlite3
        try:
            con = sqlite3.connect('sms.db')
            cur = con.cursor()
            cur.execute('SELECT COUNT(*) FROM employee')
            emp_count = cur.fetchone()[0]
            cur.execute('SELECT COUNT(*) FROM supplier')
            sup_count = cur.fetchone()[0]
            cur.execute('SELECT COUNT(*) FROM category')
            cat_count = cur.fetchone()[0]
            cur.execute('SELECT COUNT(*) FROM product')
            prod_count = cur.fetchone()[0]
            # For sales, count files in bill/ directory
            import os
            sales_count = 0
            if os.path.exists('bill'):
                sales_count = len([f for f in os.listdir('bill') if f.endswith('.txt')])
            # Developer count is static (set to 1 or 0)
            dev_count = 1
            self.lbl_employee.config(text=f"Total Employee\n[{emp_count}]")
            self.lbl_supplier.config(text=f"Total Supplier\n[{sup_count}]")
            self.lbl_category.config(text=f"Total Category\n[{cat_count}]")
            self.lbl_product.config(text=f"Total Product\n[{prod_count}]")
            self.lbl_sales.config(text=f"Total Sales\n[{sales_count}]")
            self.lbl_developer.config(text=f"Developer\n[{dev_count}]")
            con.close()
        except Exception as ex:
            # Optionally, show error or log
            pass
        self.root.after(3000, self.update_dashboard_counts)  # Update every 3 seconds

    def add_employee_window(self):
        from employee import employeeClass
        win = Toplevel(self.root)
        win.title('Employee Management')
        win.geometry('1100x500+220+130')
        win.config(bg='white')
        employeeClass(win)

    def logout(self):
        self.root.destroy()
        import login
        import tkinter as tk
        root = tk.Tk()
        login.LoginWindow(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = SMS(root)
    root.mainloop()
