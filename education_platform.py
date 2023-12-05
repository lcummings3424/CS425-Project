import psycopg2
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Label, StringVar

con = psycopg2.connect(
    database="test",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
)
cursor_obj = con.cursor()
email = ""
check_upd1 = False


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page1, Page2, Page3):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.update()
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        r = self
        self.controller = controller
        label = ttk.Label(self, text="Email: ")
        label2 = ttk.Label(self, text="Password: ")
        label.pack(side="top")
        entry1 = ttk.Entry(r, width=30)
        entry2 = ttk.Entry(r, width=30)
        self.winfo_toplevel().title("Education Platform")
        entry1.pack(pady=10, side="top")
        label2.pack(side="top")
        entry2.pack(pady=10, side="top")

        def login_click():
            username = entry1.get()
            password = entry2.get()
            global email
            email = username
            check = f"SELECT EXISTS(SELECT 1 FROM users WHERE email = '{username}' AND hashed_password = '{password}')"
            cursor_obj.execute(check)
            result = cursor_obj.fetchall()
            result = result[0][0]
            if result == True:
                self.controller.show_frame(Page1)
            else:
                messagebox.showerror(
                    "ERROR", "That email and password combination does not exist"
                )

        def create_click():
            self.controller.show_frame(Page3)

        button = tk.Button(r, text="Login", width=25, command=login_click)
        button.pack()

        button2 = tk.Button(r, text="Create Account", width=25, command=create_click)
        button2.pack()


class Page1(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller

        global check_upd1

        # def b2_click():
        #     global check_upd1
        #     check_upd1 = False
        #     self.controller.show_frame(StartPage)

        tk.Frame.__init__(self, parent)
        self.winfo_toplevel().title("Education Platform")
        # button2 = ttk.Button(self, text="Back", command=b2_click)
        # button2.pack()
        button1 = ttk.Button(
            self, text="Profile", command=lambda: controller.show_frame(Page2)
        )
        button1.pack()


class Page2(tk.Frame):
    global email
    global check_upd1

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.winfo_toplevel().title("Education Platform")

        button1 = ttk.Button(
            self, text="Back", command=lambda: controller.show_frame(Page1)
        )
        button1.pack()

    def update(self):
        global check_upd1
        if not check_upd1:
            check_upd1 = True
            sql = f"SELECT * FROM users WHERE email = '{email}';"
            cursor_obj.execute(sql)
            result = cursor_obj.fetchall()
            id = result[0][0]
            first = result[0][1]
            middle = result[0][2]
            last = result[0][3]
            em = result[0][4]
            pw = result[0][5]
            jd = result[0][6]
            jt = result[0][7]
            ph = result[0][8]

            label_id = ttk.Label(self, text=f"ID: {id}")
            label_first = ttk.Label(self, text=f"First Name: {first}")
            label_middle = ttk.Label(self, text=f"Middle Name: {middle}")
            label_last = ttk.Label(self, text=f"Last Name: {last}")
            label_em = ttk.Label(self, text=f"Email: {em}")
            label_pw = ttk.Label(self, text=f"Password: {pw}")
            label_jd = ttk.Label(self, text=f"Join Date: {jd}")
            label_jt = ttk.Label(self, text=f"Join Time: {jt}")
            label_ph = ttk.Label(self, text=f"Phone: {ph}")

            label_id.pack()
            label_first.pack()
            label_middle.pack()
            label_last.pack()
            label_em.pack()
            label_pw.pack()
            label_jd.pack()
            label_jt.pack()
            label_ph.pack()


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        def create_click():
            maxSql = "SELECT max(user_id)FROM users"
            cursor_obj.execute(maxSql)
            maxID = cursor_obj.fetchall()[0][0]
            ID = maxID + 1
            email = entry1.get()
            pw = entry2.get()
            fn = entry3.get()
            mn = entry4.get()
            ln = entry5.get()
            ph = entry6.get()
            insertSQL = f"""INSERT INTO users 
                            (user_id,first_name,middle_name,last_name,email,hashed_password,phone) 
                            VALUES
                            ({ID},'{fn}','{mn}','{ln}','{email}','{pw}',{ph})"""
            cursor_obj.execute(insertSQL)
            con.commit()
            messagebox.showinfo("Notice", "Account has been successfully created")
            self.controller.show_frame(StartPage)

        tk.Frame.__init__(self, parent)
        self.winfo_toplevel().title("Education Platform")
        r = self
        self.controller = controller
        label = ttk.Label(self, text="Email: ")
        label2 = ttk.Label(self, text="Password: ")
        label.pack(side="top")
        entry1 = ttk.Entry(r, width=30)
        entry2 = ttk.Entry(r, width=30)
        self.winfo_toplevel().title("Education Platform")
        entry1.pack(pady=10, side="top")
        label2.pack(side="top")
        entry2.pack(pady=10, side="top")
        entry3 = ttk.Entry(r, width=30)
        entry4 = ttk.Entry(r, width=30)
        entry5 = ttk.Entry(r, width=30)
        entry6 = ttk.Entry(r, width=30)
        label = ttk.Label(self, text="First name: ")
        label.pack(side="top")
        entry3.pack(pady=10, side="top")
        label = ttk.Label(self, text="Middle name: ")
        label.pack(side="top")
        entry4.pack(pady=10, side="top")
        label = ttk.Label(self, text="Last name: ")
        label.pack(side="top")
        entry5.pack(pady=10, side="top")
        label = ttk.Label(self, text="Phone number: ")
        label.pack(side="top")
        entry6.pack(pady=10, side="top")
        button2 = tk.Button(r, text="Create Account", width=25, command=create_click)
        button2.pack()


app = tkinterApp()
app.title = "Education Platform"
app.geometry("1280x720")
app.mainloop()
