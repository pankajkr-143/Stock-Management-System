from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3

class productClass:
    def __init__(self,root):
        pass
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("TITE Stock Management System")
        self.root.config(bg="white")
        self.root.focus_force()

##############################################################
        #All Variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_pid=StringVar()
        self.var_category=StringVar()
        self.var_supplier=StringVar()
        self.category_list=[]
        self.supplier_list=[]
        self.fetch_category_supplier()

        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()

        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)
        
        #title
        title=Label(product_Frame,text="Product Details",font=("times new roman",18,"bold"),bg="#ff0000",fg="white").pack(side=TOP,fill=X)

        lbl_category=Label(product_Frame,text="Category: ",font=("times new roman",18,"bold"),bg="white").place(x=30,y=60)
        lbl_supplier=Label(product_Frame,text="Supplier: ",font=("times new roman",18,"bold"),bg="white").place(x=30,y=110)
        lbl_name=Label(product_Frame,text="Name: ",font=("times new roman",18,"bold"),bg="white").place(x=30,y=160)
        lbl_price=Label(product_Frame,text="Price: ",font=("times new roman",18,"bold"),bg="white").place(x=30,y=210)
        lbl_qty=Label(product_Frame,text="QTY: ",font=("times new roman",18,"bold"),bg="white").place(x=30,y=260)
        lbl_status=Label(product_Frame,text="Status: ",font=("times new roman",18,"bold"),bg="white").place(x=30,y=310)
 
        #txt_category=Label(product_Frame,text="Category: ",font=("times new roman",18,"bold"),bg="white").place(x=30,y=60)
 
        #options
        cmb_category=ttk.Combobox(product_Frame,textvariable=self.var_category,values=self.category_list,state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_category.place(x=150,y=60,width=200)
        cmb_category.current(0)
        
        cmb_supplier=ttk.Combobox(product_Frame,textvariable=self.var_supplier,values=self.supplier_list,state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_supplier.place(x=150,y=110,width=200)
        cmb_supplier.current(0)
        
        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("times new roman",15,"bold"),bg="white").place(x=150,y=160,width=200)
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("times new roman",15,"bold"),bg="white").place(x=150,y=210,width=200)
        txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=("times new roman",15,"bold"),bg="white").place(x=150,y=260,width=200)
        #txt_status=Entry(product_Frame,textvariable=self.var_status,font=("times new roman",15,"bold"),bg="white").place(x=150,y=310,width=200)

        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Select","Active","Deactive"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)
        
        
        #buttons
        btn_add=Button(product_Frame,text="Save",command=self.add,font=("times new roman",20,"bold"),bg="#301934",fg="white",cursor="hand2").place(x=10,y=400,height=40,width=100)
        btn_update=Button(product_Frame,text="Update",command=self.update,font=("times new roman",20,"bold"),bg="#000080",fg="white",cursor="hand2").place(x=120,y=400,height=40,width=100)
        btn_delete=Button(product_Frame,text="Delete",command=self.delete,font=("times new roman",20,"bold"),bg="#FFA500",fg="white",cursor="hand2").place(x=230,y=400,height=40,width=100)
        btn_clear=Button(product_Frame,text="Clear",command=self.clear,font=("times new roman",20,"bold"),bg="#0000FF",fg="white",cursor="hand2").place(x=340,y=400,height=40,width=100)

        #searchFrame        
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)
        
        #options
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Name","Category","Supplier"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("times new roman",20,"bold"),bg="#000080",fg="white",cursor="hand2").place(x=410,y=9,height=30,width=150)

        #Product Deails
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)
        
        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)
        
        self.ProductTable=ttk.Treeview(p_frame,columns=("pid","Category","Supplier","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        self.ProductTable.heading("pid",text="PRODUCT ID")
        self.ProductTable.heading("Category",text="CATEGORY")
        self.ProductTable.heading("Supplier",text="SUPPLIER")
        self.ProductTable.heading("name",text="NAME")
        self.ProductTable.heading("price",text="PRICE")
        self.ProductTable.heading("qty",text="QTY")
        self.ProductTable.heading("status",text="STATUS")
        
        self.ProductTable["show"]="headings"
        
        self.ProductTable.column("pid",width=90)
        self.ProductTable.column("Category",width=100)
        self.ProductTable.column("Supplier",width=100)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("price",width=100)
        self.ProductTable.column("qty",width=100)
        self.ProductTable.column("status",width=100)
        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
        

######################### save ##############################################
    def fetch_category_supplier(self):
        self.category_list.append("Empty")
        self.supplier_list.append("Empty")

        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("Select name from category")
            category=cur.fetchall()
            if len(category)>0:
                del self.category_list[:]
                self.category_list.append("Select")
                for i in category:
                    self.category_list.append(i[0])
            
            cur.execute("Select name from supplier")
            supplier=cur.fetchall()
            if len(supplier)>0:
                del self.supplier_list[:]
                self.supplier_list.append("Select")
                for i in supplier:
                    self.supplier_list.append(i[0])
            

            
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       
    
    
    
    def add(self):  
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_category.get()=="Select" or self.var_category.get()=="Empty" or self.var_supplier.get()=="Select" or self.var_name.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Product already available, try different",parent=self.root)
                else:
                    cur.execute("Insert into product(Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?)",(
                                                                                self.var_category.get(),
                                                                                self.var_supplier.get(),
                                                                                self.var_name.get(),
                                                                                self.var_price.get(),
                                                                                self.var_qty.get(),
                                                                                self.var_status.get(),
                                                                                
                                                                                
                    ))
                    
                
                    con.commit()
                    messagebox.showinfo("Success","Product Addedd Successfully",parent=self.root)
                    self.show()
                                

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       
    
    ###########data fatching########
    
    def show(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)
              
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       
    
    
    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        #print(row)
        self.var_pid.set(row[0]),
        self.var_category.set(row[1]),
        self.var_supplier.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6]),
    
    
    ######## Update #################
    def update(self):  
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please select product from list",parent=self.root)
            
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid product id",parent=self.root)
                else:
                    cur.execute("Update product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=?",(
                                                                                self.var_category.get(),
                                                                                self.var_supplier.get(),
                                                                                self.var_name.get(),
                                                                                self.var_price.get(),
                                                                                self.var_qty.get(),
                                                                                self.var_status.get(),
                                                                                self.var_pid.get()

                    ))
                    
                
                    con.commit()
                    messagebox.showinfo("Success","Product Updated Successfully",parent=self.root)
                    self.show()
                                

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       
    
    
    ################# DELETE ####################
    def delete(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please select product fom the list",parent=self.root)
            
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       
    
    ##################### CLEAR #############################
    def clear(self):
        self.var_category.set(""),
        self.var_supplier.set(""),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set(""),
        self.var_pid.set(""),
        self.var_searchtxt.set("") 
        self.var_searchby.set("Select")
        self.show()
    
    ################### Search ##################
    def search(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error", "Select Search by options",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Search area should be required",parent=self.root)
            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!",parent=self.root)
              
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       
           
        
        
if __name__=="__main__":      
    root=Tk()
    obj=productClass(root)
    root.mainloop()