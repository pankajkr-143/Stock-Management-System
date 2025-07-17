from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3

class employeeClass:
    def __init__(self,root):
        pass
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("TITE Stock Management System")
        self.root.config(bg="#e3eafc")
        self.root.focus_force()

        # All Variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
    
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        
        self.var_salary=StringVar()
        self.var_login_user=StringVar()
        self.var_login_pass=StringVar()
        
        
        
        
        #searchFrame        
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)
        
        #options
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Name","Email","Employee ID","Contact"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("times new roman",20,"bold"),bg="#000080",fg="white",cursor="hand2").place(x=410,y=9,height=30,width=150)

        # Main frame for the form
        self.form_frame = Frame(self.root, bg='white', bd=2, relief='ridge')
        self.form_frame.place(x=20, y=20, width=1060, height=320)

        # Billing Dashboard Login Frame
        self.login_frame = Frame(self.form_frame, bg='#f5f7fa', bd=1, relief='groove')
        self.login_frame.place(x=20, y=10, width=1020, height=60)
        Label(self.login_frame, text="User Name", font=("Segoe UI", 12, "bold"), bg='#f5f7fa').place(x=100, y=10)
        Entry(self.login_frame, textvariable=self.var_login_user, font=("Segoe UI", 12), bg='white', relief='flat', highlightthickness=1, highlightbackground='#c5cae9').place(x=220, y=10, width=220, height=30)
        Label(self.login_frame, text="Password", font=("Segoe UI", 12, "bold"), bg='#f5f7fa').place(x=480, y=10)
        Entry(self.login_frame, textvariable=self.var_login_pass, font=("Segoe UI", 12), show='*', bg='white', relief='flat', highlightthickness=1, highlightbackground='#c5cae9').place(x=570, y=10, width=220, height=30)

        # Employee Details Title
        Label(self.form_frame, text="Employee Details", font=("Segoe UI", 16, "bold"), bg='white', fg='#3f51b5').place(x=20, y=75, width=1020)

        # Employee Details Grid
        # Row 1
        Label(self.form_frame, text="Emp ID:", font=("Segoe UI", 12, "bold"), bg="white").place(x=30, y=110)
        Entry(self.form_frame, textvariable=self.var_emp_id, font=("Segoe UI", 12), bg="#f5f7fa", relief='flat', highlightthickness=1, highlightbackground='#c5cae9').place(x=120, y=110, width=180, height=28)
        Label(self.form_frame, text="Gender:", font=("Segoe UI", 12, "bold"), bg="white").place(x=320, y=110)
        cmb_gender=ttk.Combobox(self.form_frame, textvariable=self.var_gender, values=("Select","Male","Female","Transgender","Other"), state="readonly", justify=CENTER, font=("Segoe UI", 12))
        cmb_gender.place(x=400, y=110, width=140, height=28)
        cmb_gender.current(0)
        Label(self.form_frame, text="Contact:", font=("Segoe UI", 12, "bold"), bg="white").place(x=570, y=110)
        Entry(self.form_frame, textvariable=self.var_contact, font=("Segoe UI", 12), bg="#f5f7fa", relief='flat', highlightthickness=1, highlightbackground='#c5cae9').place(x=650, y=110, width=180, height=28)

        # Row 2
        Label(self.form_frame, text="Name:", font=("Segoe UI", 12, "bold"), bg="white").place(x=30, y=150)
        Entry(self.form_frame, textvariable=self.var_name, font=("Segoe UI", 12), bg="#f5f7fa", relief='flat', highlightthickness=1, highlightbackground='#c5cae9').place(x=120, y=150, width=180, height=28)
        Label(self.form_frame, text="DOB:", font=("Segoe UI", 12, "bold"), bg="white").place(x=320, y=150)
        Entry(self.form_frame, textvariable=self.var_dob, font=("Segoe UI", 12), bg="#f5f7fa", relief='flat', highlightthickness=1, highlightbackground='#c5cae9').place(x=400, y=150, width=140, height=28)
        Label(self.form_frame, text="DOJ:", font=("Segoe UI", 12, "bold"), bg="white").place(x=570, y=150)
        Entry(self.form_frame, textvariable=self.var_doj, font=("Segoe UI", 12), bg="#f5f7fa", relief='flat', highlightthickness=1, highlightbackground='#c5cae9').place(x=650, y=150, width=180, height=28)

        # Row 3
        Label(self.form_frame, text="Email:", font=("Segoe UI", 12, "bold"), bg="white").place(x=30, y=190)
        Entry(self.form_frame, textvariable=self.var_email, font=("Segoe UI", 12), bg="#f5f7fa", relief='flat', highlightthickness=1, highlightbackground='#c5cae9').place(x=120, y=190, width=180, height=28)

        # Row 4
        Label(self.form_frame, text="Address:", font=("Segoe UI", 12, "bold"), bg="white").place(x=30, y=230)
        self.txt_address=Text(self.form_frame, font=("Segoe UI", 12), bg="#f5f7fa", relief='flat', highlightthickness=1, highlightbackground='#c5cae9')
        self.txt_address.place(x=120, y=230, width=300, height=50)
        Label(self.form_frame, text="Salary:", font=("Segoe UI", 12, "bold"), bg="white").place(x=450, y=230)
        Entry(self.form_frame, textvariable=self.var_salary, font=("Segoe UI", 12), bg="#f5f7fa", relief='flat', highlightthickness=1, highlightbackground='#c5cae9').place(x=520, y=230, width=180, height=28)

        # Buttons Frame
        btn_style = {'font': ("Segoe UI", 13, "bold"), 'bd': 0, 'relief': 'flat', 'activebackground': '#283593', 'activeforeground': 'white', 'cursor': 'hand2'}
        btn_frame = Frame(self.form_frame, bg='white')
        btn_frame.place(x=730, y=230, width=300, height=40)
        Button(btn_frame, text="Save", command=self.add, bg="#3f51b5", fg="white", **btn_style).pack(side=LEFT, expand=True, fill='x', padx=8)
        Button(btn_frame, text="Update", command=self.update, bg="#1976d2", fg="white", **btn_style).pack(side=LEFT, expand=True, fill='x', padx=8)
        Button(btn_frame, text="Delete", command=self.delete, bg="#FFA500", fg="white", **btn_style).pack(side=LEFT, expand=True, fill='x', padx=8)
        Button(btn_frame, text="Clear", command=self.clear, bg="#0000FF", fg="white", **btn_style).pack(side=LEFT, expand=True, fill='x', padx=8)

        # Employee Table Frame (unchanged)
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        # Correct column order: eid, name, email, gender, contact, dob, doj, address, salary, billing_user, billing_pass
        columns=("eid","name","email","gender","contact","dob","doj","address","salary","billing_user","billing_pass")
        self.EmployeeTable=ttk.Treeview(emp_frame,columns=columns,yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="NAME")
        self.EmployeeTable.heading("email",text="EMAIL")
        self.EmployeeTable.heading("gender",text="GENDER")
        self.EmployeeTable.heading("contact",text="CONTACT No.")
        self.EmployeeTable.heading("dob",text="DOB")
        self.EmployeeTable.heading("doj",text="DOJ")
        self.EmployeeTable.heading("address",text="ADDRESS")
        self.EmployeeTable.heading("salary",text="SALARY")
        self.EmployeeTable.heading("billing_user",text="Billing User")
        self.EmployeeTable.heading("billing_pass",text="Billing Pass")
        self.EmployeeTable["show"]="headings"
        self.EmployeeTable.column("eid",width=70)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=80)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=80)
        self.EmployeeTable.column("doj",width=80)
        self.EmployeeTable.column("address",width=120)
        self.EmployeeTable.column("salary",width=80)
        self.EmployeeTable.column("billing_user",width=100)
        self.EmployeeTable.column("billing_pass",width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
        
        ######################### save ##############################################
    def add(self):  
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            elif self.var_login_user.get()=="" or self.var_login_pass.get()=="":
                messagebox.showerror("Error","Billing Dashboard User Name and Password are required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","This employee id already assigned, try different",parent=self.root)
                else:
                    # Ensure salary is integer
                    salary_value = self.var_salary.get().replace(',', '').strip()
                    if salary_value == '':
                        salary_value = 0
                    else:
                        salary_value = int(salary_value)
                    cur.execute("Insert into employee(eid,name,email,gender,contact,dob,doj,pass,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                                                                self.var_emp_id.get(),
                                                                                self.var_name.get(),
                                                                                self.var_email.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_contact.get(),
                                                                                self.var_dob.get(),
                                                                                self.var_doj.get(),
                                                                                self.var_pass.get(),
                                                                                self.txt_address.get('1.0',END),
                                                                                salary_value,
                    ))
                    # Add to users table for login
                    cur.execute('''CREATE TABLE IF NOT EXISTS users (
                        id TEXT PRIMARY KEY,
                        name TEXT,
                        password TEXT,
                        role TEXT
                    )''')
                    con.commit()
                    cur.execute("SELECT * FROM users WHERE id=?", (self.var_login_user.get(),))
                    if cur.fetchone():
                        messagebox.showerror("Error","This User Name already exists in login system",parent=self.root)
                        return
                    cur.execute("INSERT INTO users (id, name, password, role) VALUES (?, ?, ?, ?)", (
                        self.var_login_user.get(),
                        self.var_name.get(),
                        self.var_login_pass.get(),
                        'Employee'))
                    con.commit()
                    messagebox.showinfo("Success","Employee Addedd Successfully",parent=self.root)
                    self.show()
                                

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       
    
    ###########data fatching########
    
    def show(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                # Fetch billing user/pass from users table
                cur.execute("SELECT id, password FROM users WHERE name=? AND role='Employee'", (row[1],))
                user_row = cur.fetchone()
                billing_user = user_row[0] if user_row else ''
                billing_pass = user_row[1] if user_row else ''
                # employee table schema: eid, name, email, gender, contact, dob, doj, pass, address, salary
                # display_row must match columns: eid, name, email, gender, contact, dob, doj, address, salary, billing_user, billing_pass
                display_row = [
                    row[0],  # eid
                    row[1],  # name
                    row[2],  # email
                    row[3],  # gender
                    row[4],  # contact
                    row[5],  # dob
                    row[6],  # doj
                    row[9],  # address
                    row[10], # salary
                    billing_user,
                    billing_pass
                ]
                self.EmployeeTable.insert('',END,values=display_row)
              
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       
    
    
    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        #print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[7])
        self.var_salary.set(row[8])
        self.var_login_user.set(row[9])
        self.var_login_pass.set(row[10])
    
    
    ######## Update #################
    def update(self):  
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            elif self.var_login_user.get()=="" or self.var_login_pass.get()=="":
                messagebox.showerror("Error","Billing Dashboard User Name and Password are required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid employee id",parent=self.root)
                else:
                    # Ensure salary is integer
                    salary_value = self.var_salary.get().replace(',', '').strip()
                    if salary_value == '':
                        salary_value = 0
                    else:
                        salary_value = int(salary_value)
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,address=?,salary=? where eid=?",(
                                                                                self.var_name.get(),
                                                                                self.var_email.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_contact.get(),
                                                                                self.var_dob.get(),
                                                                                self.var_doj.get(),
                                                                                self.var_pass.get(),
                                                                                self.txt_address.get('1.0',END),
                                                                                salary_value,
                                                                                self.var_emp_id.get(),

                    ))
                    # Update or insert billing user/pass in users table
                    cur.execute('''CREATE TABLE IF NOT EXISTS users (
                        id TEXT PRIMARY KEY,
                        name TEXT,
                        password TEXT,
                        role TEXT
                    )''')
                    con.commit()
                    cur.execute("SELECT * FROM users WHERE id=?", (self.var_login_user.get(),))
                    if cur.fetchone():
                        cur.execute("UPDATE users SET name=?, password=?, role=? WHERE id=?", (
                            self.var_name.get(),
                            self.var_login_pass.get(),
                            'Employee',
                            self.var_login_user.get()
                        ))
                    else:
                        cur.execute("INSERT INTO users (id, name, password, role) VALUES (?, ?, ?, ?)", (
                            self.var_login_user.get(),
                            self.var_name.get(),
                            self.var_login_pass.get(),
                            'Employee'))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Successfully",parent=self.root)
                    self.show()
                                

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       
    
    
    ################# DELETE ####################
    def delete(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid employee id",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       
    
    ##################### CLEAR #############################
    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.txt_address.delete('1.0',END)
        self.var_salary.set("") 
        self.var_searchtxt.set("") 
        self.var_searchby.set("Select")
        self.var_login_user.set("")
        self.var_login_pass.set("")
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
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!",parent=self.root)
              
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                       
    
            
        
        
if __name__=="__main__":      
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()