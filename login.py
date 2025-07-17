import tkinter as tk
from tkinter import messagebox
import sqlite3
from billing import BillClass
from dashboard import SMS

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Login - Stock Management System')
        self.root.geometry('480x480+500+200')
        self.root.resizable(False, False)
        self.root.config(bg='#e3eafc')  # Light blue background

        # Main frame for the login box
        self.frame = tk.Frame(self.root, bg='white', bd=2, relief='ridge')
        self.frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=370)

        self.var_role = tk.StringVar(value='Admin')
        self.var_user = tk.StringVar()
        self.var_pass = tk.StringVar()

        # Title
        tk.Label(self.frame, text='LOGIN', font=('Segoe UI', 26, 'bold'), bg='white', fg='#3f51b5').pack(pady=(18, 4), fill='x')
        # Subtitle
        tk.Label(self.frame, text='Stock Management System', font=('Segoe UI', 12, 'italic'), bg='white', fg='#607d8b').pack(pady=(0, 12), fill='x')

        # Role
        tk.Label(self.frame, text='Role', font=('Segoe UI', 12, 'bold'), bg='white', anchor='w').pack(fill='x', padx=36)
        role_menu = tk.OptionMenu(self.frame, self.var_role, 'Admin', 'Employee')
        role_menu.config(font=('Segoe UI', 11), bg='#e3eafc', fg='#3f51b5', bd=0, highlightthickness=0, activebackground='#c5cae9')
        role_menu.pack(fill='x', padx=36, pady=(0, 10))

        # User ID
        tk.Label(self.frame, text='User ID', font=('Segoe UI', 12, 'bold'), bg='white', anchor='w').pack(fill='x', padx=36)
        user_entry = tk.Entry(self.frame, textvariable=self.var_user, font=('Segoe UI', 12), bg='#f5f7fa', relief='flat', highlightthickness=1, highlightbackground='#c5cae9')
        user_entry.pack(fill='x', padx=36, pady=(0, 10), ipady=4)

        # Password
        tk.Label(self.frame, text='Password', font=('Segoe UI', 12, 'bold'), bg='white', anchor='w').pack(fill='x', padx=36)
        pass_entry = tk.Entry(self.frame, textvariable=self.var_pass, font=('Segoe UI', 12), show='*', bg='#f5f7fa', relief='flat', highlightthickness=1, highlightbackground='#c5cae9')
        pass_entry.pack(fill='x', padx=36, pady=(0, 18), ipady=4)

        # Login Button
        login_btn = tk.Button(self.frame, text='Login', font=('Segoe UI', 14, 'bold'), bg='#3f51b5', fg='white', bd=0, relief='flat', activebackground='#283593', activeforeground='white', command=self.login, cursor='hand2')
        login_btn.pack(pady=(0, 12), padx=36, fill='x', ipady=6)

        # Footer
        tk.Label(self.frame, text='© 2024 TITE | All Rights Reserved', font=('Segoe UI', 9), bg='white', fg='#b0bec5').pack(side='bottom', pady=(0, 6), fill='x')

        self.ensure_admin_exists()

    def ensure_admin_exists(self):
        con = sqlite3.connect('sms.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT,
            password TEXT,
            role TEXT
        )''')
        # Check if admin exists
        cur.execute("SELECT * FROM users WHERE role='Admin'")
        if not cur.fetchone():
            # Insert default admin
            cur.execute("INSERT INTO users (id, name, password, role) VALUES (?, ?, ?, ?)",
                        ('admin', 'Administrator', 'admin123', 'Admin'))
            con.commit()
        con.close()

    def login(self):
        uid = self.var_user.get().strip()
        pwd = self.var_pass.get().strip()
        role = self.var_role.get()
        if not uid or not pwd:
            messagebox.showerror('Error', 'All fields are required', parent=self.root)
            return
        con = sqlite3.connect('sms.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM users WHERE id=? AND password=? AND role=?', (uid, pwd, role))
        user = cur.fetchone()
        con.close()
        if user:
            self.root.destroy()
            if role == 'Admin':
                root_dash = tk.Tk()
                SMS(root_dash)
                root_dash.mainloop()
            else:
                root_bill = tk.Tk()
                BillClass(root_bill)
                root_bill.mainloop()
        else:
            messagebox.showerror('Error', 'Invalid credentials', parent=self.root)

if __name__ == '__main__':
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop() 