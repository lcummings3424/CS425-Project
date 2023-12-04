import psycopg2
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

con = psycopg2.connect(
    database="test",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
)
cursor_obj = con.cursor()

LARGEFONT = ("Verdana", 35)

email = ""


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page1, Page2):
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
        entry1 = ttk.Entry(r, width=30)
        entry2 = ttk.Entry(r, width=30)

        entry1.pack(pady=10)
        entry2.pack(pady=10)

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

        button = tk.Button(r, text="Login", width=25, command=login_click)
        button.pack()


class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = ttk.Button(
            self, text="Profile", command=lambda: controller.show_frame(Page2)
        )
        button1.pack()


class Page2(tk.Frame):
    global email

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

    def update(self):
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
        label_jt = ttk.Label(self, text=f"Job Title: {jt}")
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


app = tkinterApp()
app.title = "Education Platform"
app.geometry("1280x720")
app.mainloop()
