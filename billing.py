from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class BillClass:
    def __init__(self,root):
        pass
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("TITE Stock Management System")
        self.root.config(bg="white")
        self.cart_list=[]
        #title
        self.icon_title=PhotoImage(file="Images/logo1.png")
        title=Label(self.root,text="TITE Stock Management System",image=self.icon_title,compound=LEFT, font=("times new roman",40,"bold"),bg="#ff0000",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #button-Logout
        btn_logout=Button(self.root,text="Logout",font=("times new roman",20,"bold"),bg="#000080",fg="white",cursor="hand2").place(x=1150,y=10,height=50,width=150)
       
        #clock
        self.lbl_clock=Label(self.root,text="Welcome to Stock Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#000080",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        
        #Product Frame
        
        ProductFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame.place(x=6,y=110,width=410,height=550)
        
        pTitle=Label(ProductFrame,text="All Products",font=("times new roman",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        
        #Product Search Frame
        self.var_search=StringVar()
        ProductFrame1=Frame(ProductFrame,bd=2,relief=RIDGE,bg="white")
        ProductFrame1.place(x=2,y=42,width=398,height=90)
        
        lbl_search=Label(ProductFrame1,text="Search Product | By Name ",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=2,y=5)
        
        lbl_search=Label(ProductFrame1,text="Product Name ",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        txt_search=Entry(ProductFrame1,textvariable=self.var_search,font=("times new roman",15,),bg="lightyellow").place(x=128,y=47,width=150,height=22)
        btn_search=Button(ProductFrame1,text="Search",command=self.search,font=("times new roman",15,"bold"),bg="pink",fg="blue",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show=Button(ProductFrame1,text="Show All",command=self.show,font=("times new roman",15,"bold"),bg="black",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)

        
        #Product Details Frame
        ProductFrame2=Frame(ProductFrame,bd=3,relief=RIDGE)
        ProductFrame2.place(x=2,y=140,width=398,height=378)
        
        scrolly=Scrollbar(ProductFrame2,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame2,orient=HORIZONTAL)
        
        self.productTable=ttk.Treeview(ProductFrame2,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        
        self.productTable.heading("pid",text="P ID")
        self.productTable.heading("name",text="NAME")
        self.productTable.heading("price",text="PRICE")
        self.productTable.heading("qty",text="QTY")
        self.productTable.heading("status",text="STATUS")

        
        self.productTable["show"]="headings"
        
        self.productTable.column("pid",width=40)
        self.productTable.column("name",width=100)
        self.productTable.column("price",width=100)
        self.productTable.column("qty",width=40)
        self.productTable.column("status",width=90)

        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        
        lbl_note=Label(ProductFrame,text="Note: 'Enter 0 QTY to Remove the Product from Cart'.",font=("times new roman",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)


        ######  Customer Frame ###### 
        
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)
        
        cTitle=Label(CustomerFrame,text="Customer Details",font=("times new roman",14,"bold"),bg="lightpink",fg="blue").pack(side=TOP,fill=X)

        lbl_name=Label(CustomerFrame,text="Name ",font=("times new roman",15),bg="white").place(x=0,y=30)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",13,),bg="lightyellow").place(x=65,y=35,width=150)

        lbl_contact=Label(CustomerFrame,text="Contact No. ",font=("times new roman",15),bg="white").place(x=240,y=30)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13,),bg="lightyellow").place(x=350,y=35,width=150)


        Cal_CartFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Cal_CartFrame.place(x=420,y=190,width=530,height=360)
        
        
        #calculator frame
        self.var_cal_input=StringVar()
        
        CalFrame=Frame(Cal_CartFrame,bd=9,relief=RIDGE,bg="white")
        CalFrame.place(x=5,y=10,width=268,height=340)
        
        txt_cal_input=Entry(CalFrame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)
        
        btn_7=Button(CalFrame,text='7',font=('arial',15,'bold'),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(CalFrame,text='8',font=('arial',15,'bold'),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(CalFrame,text='9',font=('arial',15,'bold'),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(CalFrame,text='+',font=('arial',15,'bold'),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)


        btn_4=Button(CalFrame,text='4',font=('arial',15,'bold'),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(CalFrame,text='5',font=('arial',15,'bold'),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(CalFrame,text='6',font=('arial',15,'bold'),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_min=Button(CalFrame,text='-',font=('arial',15,'bold'),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)
        
        btn_1=Button(CalFrame,text='1',font=('arial',15,'bold'),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(CalFrame,text='2',font=('arial',15,'bold'),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(CalFrame,text='3',font=('arial',15,'bold'),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(CalFrame,text='*',font=('arial',15,'bold'),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)

        btn_0=Button(CalFrame,text='0',font=('arial',15,'bold'),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(CalFrame,text='C',font=('arial',15,'bold'),command=self.clear_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=1)
        btn_equ=Button(CalFrame,text='=',font=('arial',15,'bold'),command=self.perform_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(CalFrame,text='/',font=('arial',15,'bold'),command=lambda:self.get_input('/'),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=3)

        
        cartFrame=Frame(Cal_CartFrame,bd=3,relief=RIDGE)
        cartFrame.place(x=280,y=8,width=245,height=342)
        self.cartTitle=Label(cartFrame,text="Cart \t Total Products:[0]",font=("times new roman",14,"bold"),bg="lightpink",fg="blue")
        self.cartTitle.pack(side=TOP,fill=X)

        
        scrolly=Scrollbar(cartFrame,orient=VERTICAL)
        scrollx=Scrollbar(cartFrame,orient=HORIZONTAL)
        
        self.cartTable=ttk.Treeview(cartFrame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cartTable.xview)
        scrolly.config(command=self.cartTable.yview)
        
        self.cartTable.heading("pid",text="P ID")
        self.cartTable.heading("name",text="NAME")
        self.cartTable.heading("price",text="PRICE")
        self.cartTable.heading("qty",text="QTY")
        self.cartTable.heading("status",text="STATUS")

        
        self.cartTable["show"]="headings"
        
        self.cartTable.column("pid",width=90)
        self.cartTable.column("name",width=100)
        self.cartTable.column("price",width=90)
        self.cartTable.column("qty",width=50)
        self.cartTable.column("status",width=90)

        self.cartTable.pack(fill=BOTH,expand=1)
        
        #self.cartTable.bind("<ButtonRelease-1>",self.get_data)
        
        #Add cart widgets
        
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        
        Add_CartFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Add_CartFrame.place(x=420,y=550,width=530,height=110)
        
        
        lbl_p_name=Label(Add_CartFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_CartFrame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)
 
        lbl_p_price=Label(Add_CartFrame,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_CartFrame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)
 
        lbl_p_qty=Label(Add_CartFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Add_CartFrame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=130,height=22)
 
        self.lbl_inStock=Label(Add_CartFrame,text="In Stock",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)
        
        btn_clear_cart=Button(Add_CartFrame,text="Clear",font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=200,y=70,height=30,width=140)
        btn_addupdate_cart=Button(Add_CartFrame,text="Add/Update Cart",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="lightpink",cursor="hand2").place(x=350,y=70,height=30,width=170)

        
        ###############Billing Area #########
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billFrame.place(x=953,y=110,width=400,height=410)
        
        bTitle=Label(billFrame,text="Customer Bill Area",font=("times new roman",20,"bold"),bg="red",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        
        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        
        ############Billing Buttons############
        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billMenuFrame.place(x=953,y=520,width=400,height=140)

        self.lbl_menu_btn=Label(billMenuFrame,text='Bill Amount\n[0]',font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_menu_btn.place(x=2,y=5,width=120,height=70)
        
        self.lbl_menu_btn1=Label(billMenuFrame,text='Discount\n[10%]',font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white")
        self.lbl_menu_btn1.place(x=124,y=5,width=120,height=70)
        
        self.lbl_menu_btn2=Label(billMenuFrame,text='Net Pay\n[0]',font=("goudy old style",15,"bold"),bg="#607d8b",fg="white")
        self.lbl_menu_btn2.place(x=246,y=5,width=150,height=70)
        
        menu_btn=Button(billMenuFrame,text='Print',cursor='hand2',font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        menu_btn.place(x=2,y=80,width=120,height=50)
        
        menu_btn1=Button(billMenuFrame,text='Clear All',cursor='hand2',font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white")
        menu_btn1.place(x=124,y=80,width=120,height=50)
        
        menu_btn2=Button(billMenuFrame,text='Generate/Save Bill',cursor='hand2',font=("goudy old style",12,"bold"),bg="#607d8b",fg="white")
        menu_btn2.place(x=246,y=80,width=150,height=50)
        
        #footer
        lbl_footer=Label(self.root,text="SMS-Stock Management System | Developed By: Pankaj Kumar\nIf You are facing any type of technical error then contact us! - Email-mackystech@gmail.com; Mobile: +91-82359-10315",font=("times new roman",12),bg="#000080",fg="white").pack(side=BOTTOM,fill=X)
        
        self.show()

##############Functionality############
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
    
    def clear_cal(self):
        self.var_cal_input.set('') 
    
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("select pid,name,price,qty,status from product where status='Active'")
            rows=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END,values=row)
              
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       
        
    
    def search(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error", "Search area should be required",parent=self.root)
            else:
                cur.execute("select pid,name,price,qty,status from product where name LIKE '%"+self.var_search.get()+"%' and status='Active'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!",parent=self.root)
              
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       


    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock: [{str(row[3])}]")


    def add_update_cart(self):
        if self.var_pid.get()=="":
            messagebox.showerror("Error","Please select product",parent=self.root)
        elif self.var_qty.get()=="":
            messagebox.showerror("Error","Quantity should be required",parent=self.root)
        else:
            price_cal=int(self.var_qty.get())*float(self.var_price.get())
            price_cal=float(price_cal) 
            card_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get()]          
            
            #update cart
            present="no"
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present="yes"
                    break
                index_+=1
            if present=="yes":
                op=messagebox.askyesno("Confirm","Product is already present in cart. Do you want to update it?",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        del self.cart_list[index_]
                    else:
                        self.cart_list[index_][3]=self.var_qty.get()
                        self.cart_list[index_][2]=price_cal
            else:
                self.cart_list.append(card_data)

            self.show_cart()
            self.bill_updates()


    def bill_updates(self):
        bill_amount=0
        net_pay=0
        for row in self.cart_list:
            bill_amount+=float(row[2])

        net_pay=(bill_amount*10)/100
        self.lbl_menu_btn.config(text=f"Bill Amount\n{str(bill_amount)}")
        self.lbl_menu_btn1.config(text=f"Discount\n{str(net_pay)}")
        self.lbl_menu_btn2.config(text=f"Net Pay\n{str(bill_amount-net_pay)}")
        self.cartTitle.config(text=f"Cart \t Total Products:[{str(len(self.cart_list))}]")





    def show_cart(self):
        try:
            self.cartTable.delete(*self.cartTable.get_children())
            for i in self.cart_list:
                self.cartTable.insert('',END,values=i)
            self.var_pid.set('')
            self.var_pname.set('')
            self.var_price.set('')
            self.var_qty.set('')
            self.lbl_inStock.config(text='In Stock')
            self.var_cal_input.set('')
            self.var_search.set('')
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

        


if __name__=="__main__":      
    root=Tk()
    obj=BillClass(root)
    root.mainloop()