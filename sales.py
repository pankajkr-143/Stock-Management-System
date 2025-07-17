from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os

class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("TITE Stock Management System - Sales")
        self.root.config(bg="white")
        self.root.focus_force()

        # Variables
        self.bill_area = []
        self.var_invoice = StringVar()

        # Title
        lbl_title = Label(self.root, text="View Customer Bills", font=("times new roman", 30), bg="#87CEEB", fg="white", bd=3, relief=RIDGE)
        lbl_title.pack(side=TOP, fill=X, pady=20, padx=10)

        # Invoice Input
        lbl_invoice = Label(self.root, text="Invoice No.:", font=("times new roman", 15), bg="white")
        lbl_invoice.place(x=50, y=100)
        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("times new roman", 15), bg="lightyellow")
        txt_invoice.place(x=160, y=100, width=170, height=28)

        # Search and Clear Buttons
        btn_search = Button(self.root, text="Search", command=self.search, font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2")
        btn_search.place(x=360, y=100, width=120, height=28)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("times new roman", 15, "bold"), bg="#FFC0CB", fg="white", cursor="hand2")
        btn_clear.place(x=490, y=100, width=120, height=28)

        # Sales List
        sales_Frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_Frame.place(x=50, y=140, width=200, height=330)

        scrolly = Scrollbar(sales_Frame, orient=VERTICAL)
        self.sales_list = Listbox(sales_Frame, bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH, expand=1)
        self.sales_list.bind("<ButtonRelease-1>", self.get_data)

        # Bill Area
        bill_Frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_Frame.place(x=280, y=140, width=410, height=330)

        lbl_title2 = Label(bill_Frame, text="Customer Billing Area", font=("times new roman", 20), bg="#87CEEB")
        lbl_title2.pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_list = Text(bill_Frame, font=("times new roman", 15), bg="lightyellow", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_list.yview)
        self.bill_list.pack(fill=BOTH, expand=1)

        # Monetization: Total Sales Area
        monetization_Frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        monetization_Frame.place(x=720, y=140, width=330, height=150)

        lbl_total_sales = Label(monetization_Frame, text="Total Sales", font=("times new roman", 20, "bold"), bg="#87CEEB", fg="white")
        lbl_total_sales.pack(side=TOP, fill=X)

        self.lbl_total_amount = Label(monetization_Frame, text="₹ 0.00", font=("times new roman", 30, "bold"), bg="white", fg="#000080")
        self.lbl_total_amount.pack(side=TOP, pady=20)

        # Show Bill Data
        self.show()

    ##################################################
    # Show all bills in the directory
    def show(self):
        del self.bill_area[:]
        self.sales_list.delete(0, END)
        for i in os.listdir('bill'):
            if i.split('.')[-1] == 'txt':
                self.sales_list.insert(END, i)
                self.bill_area.append(i.split('.')[0])

    # Display selected bill details
    def get_data(self, ev):
        index_ = self.sales_list.curselection()
        file_name = self.sales_list.get(index_)
        self.bill_list.delete('1.0', END)
        with open(f'bill/{file_name}', 'r') as fp:
            for line in fp:
                self.bill_list.insert(END, line)

        # Update total amount based on the bill data
        self.calculate_total(file_name)

    # Search a specific invoice
    def search(self):
        if self.var_invoice.get() == "":
            messagebox.showerror("Error", "Invoice no. should be required", parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_area:
                self.bill_list.delete('1.0', END)
                with open(f'bill/{self.var_invoice.get()}.txt', 'r') as fp:
                    for line in fp:
                        self.bill_list.insert(END, line)

                # Update total amount for the searched bill
                self.calculate_total(f"{self.var_invoice.get()}.txt")
            else:
                messagebox.showerror("Error", "Invalid Invoice No", parent=self.root)

    # Clear the displayed data
    def clear(self):
        self.show()
        self.bill_list.delete('1.0', END)
        self.lbl_total_amount.config(text="₹ 0.00")

    # Calculate the total sales amount from the bill
    def calculate_total(self, file_name):
        try:
            total = 0.0
            with open(f'bill/{file_name}', 'r') as fp:
                for line in fp:
                    if "Total Amount" in line:  # Assuming the bill contains a line with "Total Amount: <amount>"
                        amount = float(line.split(":")[-1].strip())
                        total += amount
            self.lbl_total_amount.config(text=f"₹ {total:.2f}")
        except Exception as ex:
            messagebox.showerror("Error", f"Error in calculating total: {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()
