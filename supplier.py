from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3

class supplierClass:
    def __init__(self,root):
        pass
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("TITE Stock Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #All Variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
    
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        
        
        
        
        
        
        #searchFrame        
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)
        
        #options
        lbl_search=Label(SearchFrame,text="Search by Invoice No.",bg="white",font=("goudy old style",15))
        lbl_search.place(x=10,y=10,width=180)
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("times new roman",20,"bold"),bg="#000080",fg="white",cursor="hand2").place(x=410,y=9,height=30,width=150)

        #title
        title=Label(self.root,text="Supplier Details",font=("times new roman",15,"bold"),bg="#ff0000",fg="white").place(x=50,y=100,width=1000)

        
        #Content
        lbl_supplier_invoice=Label(self.root,text="Invoice No.:",font=("times new roman",15,"bold"),bg="white").place(x=50,y=150)
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("times new roman",15,"bold"),bg="white").place(x=150,y=150,width=180)        
        
        lbl_name=Label(self.root,text="Name:",font=("times new roman",15,"bold"),bg="white").place(x=50,y=190)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15,"bold"),bg="white").place(x=150,y=190,width=180)
        
        lbl_contact=Label(self.root,text="Contact No.:",font=("times new roman",15,"bold"),bg="white").place(x=50,y=230)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15,"bold"),bg="white").place(x=150,y=230,width=180)
        
        lbl_desc=Label(self.root,text="Description:",font=("times new roman",15,"bold"),bg="white").place(x=50,y=270)
        self.txt_desc=Text(self.root,font=("times new roman",15,"bold"),bg="white")
        self.txt_desc.place(x=150,y=270,width=300,height=60)

        
        #buttons
        btn_add=Button(self.root,text="Save",command=self.add,font=("times new roman",20,"bold"),bg="#301934",fg="white",cursor="hand2").place(x=500,y=305,height=28,width=110)
        btn_update=Button(self.root,text="Update",command=self.update,font=("times new roman",20,"bold"),bg="#000080",fg="white",cursor="hand2").place(x=620,y=305,height=28,width=110)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times new roman",20,"bold"),bg="#FFA500",fg="white",cursor="hand2").place(x=740,y=305,height=28,width=110)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",20,"bold"),bg="#0000FF",fg="white",cursor="hand2").place(x=860,y=305,height=28,width=110)
        
        
        #Employee Deails
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)
        
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.SupplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        
        self.SupplierTable.heading("invoice",text="INVOICE No.")
        self.SupplierTable.heading("name",text="NAME")
        self.SupplierTable.heading("contact",text="CONTACT No.")
        self.SupplierTable.heading("desc",text="DESCRIPTION")
        
        self.SupplierTable["show"]="headings"
        
        self.SupplierTable.column("invoice",width=90)
        self.SupplierTable.column("name",width=100)
        self.SupplierTable.column("contact",width=100)
        self.SupplierTable.column("desc",width=100)
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
        
        ######################### save ##############################################
    def add(self):  
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
            
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","This Invoice No. already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into supplier(invoice,name,contact,desc) values(?,?,?,?)",(
                                                                                self.var_sup_invoice.get(),
                                                                                self.var_name.get(),

                                                                                self.var_contact.get(),
                                                                                self.txt_desc.get('1.0',END),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Addedd Successfully",parent=self.root)
                    self.show()
                                

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       
    
    ###########data fatching########
    
    def show(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
              
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       
    
    
    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        #print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[3]) 
    
    
    ######## Update #################
    def update(self):  
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
            
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                                                                                self.var_name.get(),
                                                                                self.var_contact.get(),
                                                                                self.txt_desc.get('1.0',END),
                                                                                self.var_sup_invoice.get(),
                    ))
                    
                
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
                    self.show()
                                

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       
    
    
    ################# DELETE ####################
    def delete(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Envoice No. must be required",parent=self.root)
            
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Supplier Number",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       
    
    ##################### CLEAR #############################
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0',END) 
        self.var_searchtxt.set("") 
        self.show()
    
    ################### Search ##################
    def search(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Invoice No. should be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?", (self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row != None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!",parent=self.root)
              
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       
    
            
        
        
if __name__=="__main__":      
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()