import psycopg2
import tkinter as tk
import copy
from tkinter import ttk
from tkinter import messagebox
from tkinter import Label, StringVar

# con = psycopg2.connect(
#     database="test",
#     user="postgres",
#     password="postgres",
#     host="localhost",
#     port="5432",
# )
con = psycopg2.connect(
    "postgres://nh_lc_educationplatform_user:ctX1mTYO5izqzBT38CShz4ZknhCeUmA4@dpg-clprccbd3o9c73evjtlg-a.ohio-postgres.render.com/nh_lc_educationplatform"
)
cursor_obj = con.cursor()
email = ""
check_upd1 = False
descNum = 0
userID = 0
quizNum = 0
flashCardSetNum = 0


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (
            StartPage,
            HomePage,
            ProfilePage,
            AccountCreationPage,
            AdminLoginPage,
            ContentPage,
            ContentDescPage,
            AOFInfo,
            QuizHomePage,
            QuizTakenPage,
            QuizNotTakenPage,
            TakeQuizPage,
            TakeQuiz,
            FlashcardHomePage,
            FlashcardPage,
        ):
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
            global userID
            username = entry1.get()
            password = entry2.get()
            global email
            email = username
            check = f"SELECT EXISTS(SELECT 1 FROM users WHERE email = '{username}' AND hashed_password = '{password}')"
            cursor_obj.execute(check)
            result = cursor_obj.fetchall()
            result = result[0][0]
            if result == True:
                self.controller.show_frame(HomePage)
            else:
                messagebox.showerror(
                    "ERROR", "That email and password combination does not exist"
                )

        def create_click():
            self.controller.show_frame(AccountCreationPage)

        button = tk.Button(r, text="Login", width=25, command=login_click)
        button.pack()

        button2 = tk.Button(r, text="Create Account", width=25, command=create_click)
        button2.pack()
        button3 = tk.Button(
            r,
            text="Admin Login",
            width=25,
            command=lambda: controller.show_frame(AdminLoginPage),
        )
        button3.pack()


class HomePage(tk.Frame):
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
            self, text="Profile", command=lambda: controller.show_frame(ProfilePage)
        )
        button1.pack()
        button2 = ttk.Button(
            self, text="Content", command=lambda: controller.show_frame(ContentPage)
        )
        button2.pack()
        button3 = ttk.Button(
            self, text="Quizzes", command=lambda: controller.show_frame(QuizHomePage)
        )
        button3.pack()
        button4 = ttk.Button(
            self,
            text="Flashcards",
            command=lambda: controller.show_frame(FlashcardHomePage),
        )
        button4.pack()


class ProfilePage(tk.Frame):
    global email
    global check_upd1

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.winfo_toplevel().title("Education Platform")

        button1 = ttk.Button(
            self, text="Back", command=lambda: controller.show_frame(HomePage)
        )
        button1.pack()

    def update(self):
        global check_upd1
        global userID
        if not check_upd1:
            check_upd1 = True
            sql = f"SELECT * FROM users WHERE email = '{email}';"
            cursor_obj.execute(sql)
            result = cursor_obj.fetchall()
            id = result[0][0]
            userID = id
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
            sql2 = f"""
            select * 
            from referred join users
            on referred.user_id = users.user_id
            where referred.user_id = {id}
            """
            cursor_obj.execute(sql2)
            res = cursor_obj.fetchall()
            if len(res) != 0:
                refID = res[0][1]
                sql3 = f"""
                select first_name, last_name
                from users 
                where user_id = {refID}
                """
                cursor_obj.execute(sql3)
                res2 = cursor_obj.fetchall()
                label = ttk.Label(self, text=f"Referred by: {res2[0][0]} {res2[0][1]}")
                label.pack()
            else:
                label = ttk.Label(self, text=f"Referred by: N")

        def userStats():
            countSQL = """
            select count(user_id)
            from users
            """
            cursor_obj.execute(countSQL)
            res1 = cursor_obj.fetchall()

            refSQL = """
            select count(user_id)
            from referred
            """
            cursor_obj.execute(refSQL)
            res2 = cursor_obj.fetchall()

            refGroupSQL = """
            select referred_by, count(user_id)
            from referred
            group by referred_by
            """
            cursor_obj.execute(refGroupSQL)
            res3 = cursor_obj.fetchall()
            str = ""
            str = str + f"Number of users: {res1[0][0]}"
            str = str + f"\nNumber of users that have been referred: {res2[0][0]}"
            str = str + f"\nUsers and how many others they have referred: \n"
            for i in range(len(res3)):
                temp = res3[i]
                uID = temp[0]
                ct = temp[1]
                str = str + f"User ID {uID} has referred {ct} other users\n"
            # print()
            messagebox.showinfo("User Stats", str)

        button2 = tk.Button(self, text="User Stats", width=25, command=userStats)
        button2.pack()


class AccountCreationPage(tk.Frame):
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
            if mn != "":
                insertSQL = f"""INSERT INTO users 
                                (user_id,first_name,middle_name,last_name,email,hashed_password,phone) 
                                VALUES
                                ({ID},'{fn}','{mn}','{ln}','{email}','{pw}',{ph})"""
            else:
                insertSQL = f"""INSERT INTO users 
                                (user_id,first_name,last_name,email,hashed_password,phone) 
                                VALUES
                                ({ID},'{fn}','{ln}','{email}','{pw}',{ph})"""
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
        label = ttk.Label(self, text="Middle name (optional): ")
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


class AdminLoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        r = self
        self.controller = controller
        label = ttk.Label(self, text="Email: ")
        label2 = ttk.Label(self, text="Password: ")
        label3 = ttk.Label(self, text="Admin Code: ")
        label.pack(side="top")
        entry1 = ttk.Entry(r, width=30)
        entry2 = ttk.Entry(r, width=30)
        entry3 = ttk.Entry(r, width=30)
        self.winfo_toplevel().title("Education Platform")
        entry1.pack(pady=10, side="top")
        label2.pack(side="top")
        entry2.pack(pady=10, side="top")
        label3.pack(side="top")
        entry3.pack(pady=10, side="top")

        def login_click():
            username = entry1.get()
            password = entry2.get()
            ac = entry3.get()
            global email
            email = username
            check = f"SELECT EXISTS(SELECT 1 FROM admin_users WHERE email = '{username}' AND hashed_password = '{password}' AND admin_code = '{ac}')"
            cursor_obj.execute(check)
            result = cursor_obj.fetchall()
            result = result[0][0]
            if result == True:
                self.controller.show_frame(HomePage)
            else:
                messagebox.showerror(
                    "ERROR", "That email and password combination does not exist"
                )

        # def create_click():
        #     self.controller.show_frame(AccountCreationPage)

        button = tk.Button(r, text="Login", width=25, command=login_click)
        button.pack()

        def back_click():
            # label1.destroy()
            # label2.destroy()
            # button.destroy()
            self.controller.show_frame(StartPage)

        # def AOFClick():
        #     # label1.destroy()
        #     # label2.destroy()
        #     # button.destroy()
        #     self.controller.show_frame(AOFInfo)

        button3 = tk.Button(self, text="Back", width=25, command=back_click)
        button3.pack()


class ContentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        sql = """
            SELECT *
            FROM contents JOIN content_type
            ON contents.content_id = content_type.content_id
            JOIN content_type_details ON content_type.content_type_id = content_type_details.content_type_id
            JOIN content_focus ON contents.content_id = content_focus.content_id
        """
        cursor_obj.execute(sql)
        result = cursor_obj.fetchall()
        # print(result)
        self.button = []
        for i in range(len(result)):
            name = result[i][1]
            mt = result[i][5]
            ct = result[i][7]
            af = result[i][9]
            label = ttk.Label(self, text=f"Media Type: {mt}")
            label.pack()
            label = ttk.Label(self, text=f"Content Type: {ct}")
            label.pack()
            label = ttk.Label(self, text=f"Content Type Description: {result[i][8]}")
            label.pack()            
            label = ttk.Label(self, text=f"Area Of Focus: {af}")
            label.pack()
            self.button.append(
                tk.Button(self, text=f"{name}", command=lambda i=i: self.open_this(i))
            )
            self.button[i].pack()

        def back_click():
            # label1.destroy()
            # label2.destroy()
            # button.destroy()
            self.controller.show_frame(HomePage)

        def AOFClick():
            # label1.destroy()
            # label2.destroy()
            # button.destroy()
            self.controller.show_frame(AOFInfo)

        button = tk.Button(self, text="Back", width=25, command=back_click)
        button.pack()

        button2 = tk.Button(
            self, text="Area Of Focus Information", width=25, command=AOFClick
        )
        button2.pack()

    def open_this(self, myNum):
        # print(myNum)
        global descNum
        descNum = myNum + 1
        self.controller.show_frame(ContentDescPage)


class ContentDescPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global descNum

    def update(self):
        global descNum
        sql = f"""
        SELECT *
        FROM contents
        WHERE content_id = {descNum}"""
        cursor_obj.execute(sql)
        result = cursor_obj.fetchall()[0]
        title = result[1]
        desc = result[2]
        label1 = ttk.Label(self, text=f"Title: {title}", wraplength=300)
        label1.pack()
        label2 = ttk.Label(self, text=f"Description: {desc}", wraplength=300)
        label2.pack()
        r = self

        def back_click():
            label1.destroy()
            label2.destroy()
            button.destroy()
            self.controller.show_frame(ContentPage)

        button = tk.Button(r, text="Back", width=25, command=back_click)
        button.pack()


class AOFInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        sql = """
        select *
        from area_of_focus
        """
        cursor_obj.execute(sql)
        result = cursor_obj.fetchall()
        for i in range(len(result)):
            name = result[i][0]
            desc = result[i][1]
            label = ttk.Label(self, text=f"Title: {name}")
            label.pack()
            label = ttk.Label(self, text=f"Description: {desc}")
            label.pack()

        def back_click():
            # label1.destroy()
            # label2.destroy()
            # button.destroy()
            self.controller.show_frame(ContentPage)

        def aofstat_click():
            # label1.destroy()
            # label2.destroy()
            # button.destroy()
            # self.controller.show_frame(ContentPage)
            query = """
                SELECT area_name, COUNT(content_id) AS ct
                FROM content_focus 
                GROUP BY area_name
            """
            cursor_obj.execute(query)
            result = cursor_obj.fetchall()
            query2 = f"""
            select max(ct)
            from ({query}) as foo
            """
            cursor_obj.execute(query2)
            max = cursor_obj.fetchall()[0][0]
            query3 = f"""
            select area_name 
            from ({query}) as foo
            where ct = {max}
            """
            cursor_obj.execute(query3)
            result2 = cursor_obj.fetchall()
            str = ""
            for i in range(len(result)):
                str = (
                    str + f"\nArea Name: {result[i][0]}\nContent count: {result[i][1]}"
                )
            str = str + f"\n\nArea(s) with the max number of content: "
            for i in range(len(result2)):
                str = str + f"\n{result2[i][0]},"
            messagebox.showinfo("Notice", f"Content per area of focus: \n{str}")

        button = tk.Button(self, text="Back", width=25, command=back_click)
        button.pack()

        button1 = tk.Button(self, text="Stats", width=25, command=aofstat_click)
        button1.pack()


class QuizHomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button1 = ttk.Button(
            self, text="Taken", command=lambda: controller.show_frame(QuizTakenPage)
        )
        button1.pack()
        button2 = ttk.Button(
            self,
            text="Not Taken",
            command=lambda: controller.show_frame(QuizNotTakenPage),
        )
        button2.pack()
        button2 = ttk.Button(
            self,
            text="Take a Quiz",
            command=lambda: controller.show_frame(TakeQuizPage),
        )
        button2.pack()
        button3 = ttk.Button(
            self, text="Back", command=lambda: controller.show_frame(HomePage)
        )
        button3.pack()


class QuizTakenPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def back_click():
            # label1.destroy()
            # label2.destroy()
            # button.destroy()
            for widget in QuizTakenPage.winfo_children(self):
                widget.destroy()
            # QuizHomePage.pack_forget()
            button3 = ttk.Button(self, text="Back", command=back_click)
            button3.pack()
            self.controller.show_frame(QuizHomePage)

        button3 = ttk.Button(self, text="Back", command=back_click)
        button3.pack()

    def update(self):
        sql2 = f"SELECT * FROM users WHERE email = '{email}';"
        cursor_obj.execute(sql2)
        result2 = cursor_obj.fetchall()
        id = result2[0][0]
        global userID
        userID = id
        sql = f"""
        select quiz_id, score, letter_grade 
        from taken
        where user_id = '{userID}'
        order by
        quiz_id asc
        """
        cursor_obj.execute(sql)
        result = cursor_obj.fetchall()
        self.button = []
        qid = 0
        for i in range(len(result)):
            temp = result[i]
            label = ttk.Label(self, text=f"Quiz ID: {temp[0]}", padding=(0, 15))
            label.pack()
            label = ttk.Label(self, text=f"Score: {temp[1]}")
            label.pack()
            label = ttk.Label(self, text=f"Letter Grade: {temp[2]}")
            label.pack()
            sql3 = f"""
            select passing_score 
            from quizzes 
            where quiz_id = {temp[0]}
            """
            cursor_obj.execute(sql3)
            res3 = cursor_obj.fetchall()
            temp2 = res3[0][0]
            if temp[1] < temp2:
                label = ttk.Label(self, text=f"Passed: No")
                label.pack()
            else:
                label = ttk.Label(self, text=f"Passed: Yes")
                label.pack()
            qid = copy.deepcopy(temp[0])
            self.button.append(
                tk.Button(
                    self,
                    text="Delete quiz score",
                    command=lambda i=qid: self.deleteClick(i, userID),
                )
            )
            self.button[i].pack()

    def deleteClick(self, qID, uID):
        delSQL = f"""
        delete from taken
        where user_id = {uID} and quiz_id = {qID}
        """
        cursor_obj.execute(delSQL)
        con.commit()


class QuizNotTakenPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def back_click():
            # label1.destroy()
            # label2.destroy()
            # button.destroy()
            for widget in QuizNotTakenPage.winfo_children(self):
                widget.destroy()
            # QuizHomePage.pack_forget()
            button3 = ttk.Button(self, text="Back", command=back_click)
            button3.pack()
            self.controller.show_frame(QuizHomePage)

        button3 = ttk.Button(self, text="Back", command=back_click)
        button3.pack()

    def update(self):
        sql2 = f"SELECT * FROM users WHERE email = '{email}';"
        cursor_obj.execute(sql2)
        result2 = cursor_obj.fetchall()
        id = result2[0][0]
        global userID
        userID = id
        sql0 = f"""
        select quiz_id
        from taken
        where user_id = '{userID}'
        """
        sql = f"""
        select quiz_id
        from quizzes
        where quizzes.quiz_id not in ({sql0})
        order by quiz_id asc
        """
        cursor_obj.execute(sql)
        result = cursor_obj.fetchall()
        for i in range(len(result)):
            temp = result[i]
            label = ttk.Label(self, text=f"Quiz ID: {temp[0]}", padding=(0, 15))
            label.pack()
            # label = ttk.Label(self, text=f"Score: {temp[1]}")
            # label.pack()
            # label = ttk.Label(self, text=f"Letter Grade: {temp[1]}")
            # label.pack()
            sql3 = f"""
            select passing_score 
            from quizzes 
            where quiz_id = {temp[0]}
            """
            cursor_obj.execute(sql3)
            res3 = cursor_obj.fetchall()
            label = ttk.Label(self, text=f"Passing score: {res3[0][0]}")
            label.pack()
            # temp2 = res3[0][0]
            # if temp[1] < temp2:
            #     label = ttk.Label(self, text=f"Passed: No")
            #     label.pack()
            # else:
            #     label = ttk.Label(self, text=f"Passed: Yes")
            #     label.pack()


class TakeQuizPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def update(self):
        sql2 = f"SELECT * FROM users WHERE email = '{email}';"
        cursor_obj.execute(sql2)
        result2 = cursor_obj.fetchall()
        id = result2[0][0]
        global userID
        userID = id
        sql = f"""
        select quiz_id
        from quizzes
        """
        cursor_obj.execute(sql)
        result = cursor_obj.fetchall()
        self.button = []
        for i in range(len(result)):
            temp = result[i]
            # label = ttk.Label(self, text=f"Quiz ID: {temp[0]}", padding=(0, 15))
            # label.pack()
            # label = ttk.Label(self, text=f"Score: {temp[1]}")
            # label.pack()
            # label = ttk.Label(self, text=f"Letter Grade: {temp[1]}")
            # label.pack()
            sql3 = f"""
            select passing_score, quiz_type, time_limit
            from quizzes 
            where quiz_id = {temp[0]}
            """
            cursor_obj.execute(sql3)
            res3 = cursor_obj.fetchall()
            self.button.append(
                tk.Button(
                    self, text=f"Quiz {temp[0]}", command=lambda i=i: self.open_this(i)
                )
            )
            self.button[i].pack()
            label = ttk.Label(self, text=f"Passing score: {res3[0][0]}")
            label.pack()
            label = ttk.Label(self, text=f"Quiz type: {res3[0][1]}")
            label.pack()
            label = ttk.Label(self, text=f"Time limit: {res3[0][2]} seconds")
            label.pack()
            # temp2 = res3[0][0]
            # if temp[1] < temp2:
            #     label = ttk.Label(self, text=f"Passed: No")
            #     label.pack()
            # else:
            #     label = ttk.Label(self, text=f"Passed: Yes")
            #     label.pack()

        def back_click():
            # label1.destroy()
            # label2.destroy()
            # button.destroy()
            for widget in TakeQuizPage.winfo_children(self):
                widget.destroy()
            # QuizHomePage.pack_forget()
            self.controller.show_frame(QuizHomePage)

        button3 = ttk.Button(self, text="Back", command=back_click)
        button3.pack()

    def open_this(self, myNum):
        # print(myNum)
        global quizNum
        quizNum = myNum + 1
        for widget in TakeQuizPage.winfo_children(self):
            widget.destroy()
        self.controller.show_frame(TakeQuiz)


class TakeQuiz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def update(self):
        answers = [0] * 10
        correctAnswers = [0] * 10

        def answerSelect(num, ans):
            answers[num] = ans
            # print(answers)

        self.button = []

        global quizNum
        sql = f"""
        select question_id
        from has_questions 
        where quiz_id = {quizNum}
        """
        cursor_obj.execute(sql)
        res = cursor_obj.fetchall()
        count = 0
        for i in range(len(res)):
            quID = res[i][0]
            sql2 = f"""
            select *
            from questions 
            where question_id = {quID}
            """
            cursor_obj.execute(sql2)
            res2 = cursor_obj.fetchall()
            label = ttk.Label(self, text=f"Number {i+1}: {res2[0][1]}")
            label.pack()
            correctAnswers[i] = res2[0][5]
            # label = ttk.Label(self, text=f"A: {res2[0][2]}")
            # label.pack()
            # label = ttk.Label(self, text=f"B: {res2[0][3]}")
            # label.pack()
            # label = ttk.Label(self, text=f"C: {res2[0][4]}")
            # label.pack()
            self.button.append(
                tk.Button(
                    self, text=f"{res2[0][2]}", command=lambda i=i: answerSelect(i, "A")
                )
            )
            self.button[count].pack()
            count = count + 1
            self.button.append(
                tk.Button(
                    self, text=f"{res2[0][3]}", command=lambda i=i: answerSelect(i, "B")
                )
            )
            self.button[count].pack()
            count = count + 1
            self.button.append(
                tk.Button(
                    self, text=f"{res2[0][4]}", command=lambda i=i: answerSelect(i, "C")
                )
            )
            self.button[count].pack()
            count = count + 1

        def submit():
            # label1.destroy()
            # label2.destroy()
            # button.destroy()
            finished = False
            score = 0
            sql3 = f"""
            select passing_score 
            from quizzes 
            where quiz_id = {quizNum}
            """
            cursor_obj.execute(sql3)
            res3 = cursor_obj.fetchall()
            passing = res3[0][0]
            for i in answers:
                if i == 0:
                    finished = False
                else:
                    finished = True
            if finished == False:
                messagebox.showerror("ERROR", "Quiz is not finished")
            else:
                for i in range(len(answers)):
                    if answers[i] == correctAnswers[i]:
                        score = score + 10
                if score < passing:
                    messagebox.showinfo("Results", f"Score: {score}\nPassed: No")
                else:
                    messagebox.showinfo("Results", f"Score: {score}\nPassed: Yes")
            sql4 = f"SELECT * FROM users WHERE email = '{email}';"
            cursor_obj.execute(sql4)
            result2 = cursor_obj.fetchall()
            id = result2[0][0]
            global userID
            userID = id
            sql5 = f"""
            select quiz_id, score, letter_grade 
            from taken
            where user_id = '{userID}' and quiz_id = {quizNum}
            """
            check = f"SELECT EXISTS({sql5})"
            cursor_obj.execute(check)
            taken = cursor_obj.fetchall()[0][0]
            if finished:
                letter = "F"
                if score <= 100:
                    letter = "A"
                if score <= 89:
                    letter = "B"
                if score <= 79:
                    letter = "C"
                if score <= 69:
                    letter = "D"
                if score <= 59:
                    letter = "F"
                if taken:
                    updateSQL = f"""
                    update taken
                    set score = {score},letter_grade = '{letter}'
                    where user_id = {userID} and quiz_id = {quizNum}
                    """
                    cursor_obj.execute(updateSQL)
                    con.commit()
                else:
                    insertSQL = f"""
                    insert into taken(user_id,quiz_id,score,letter_grade)
                    values({userID},{quizNum},{score},'{letter}')
                    """
                    cursor_obj.execute(insertSQL)
                    con.commit()
                for widget in TakeQuiz.winfo_children(self):
                    widget.destroy()
                # QuizHomePage.pack_forget()
                self.controller.show_frame(TakeQuizPage)

        button3 = ttk.Button(self, text="Submit", command=submit)
        button3.pack()


class FlashcardHomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        sql = """
        select *
        from flashcards join flashcard_content_type
        on flashcards.flashcard_id = flashcard_content_type.flashcard_id
        join content_type
        on flashcard_content_type.content_type_id = content_type.content_type_id
        join content_type_details
        on flashcard_content_type.content_type_id = content_type_details.content_type_id        
        """
        cursor_obj.execute(sql)
        res = cursor_obj.fetchall()
        self.button = []
        count = 1
        for i in range(len(res)):
            # p1 = copy.deepcopy(count) + 1
            # if i == 0:
            #     self.button.append(
            #         tk.Button(
            #             self,
            #             text=f"Flashcard Set {i + 1}",
            #             command=lambda i=i: self.open_this(copy.deepcopy(i)),
            #         )
            #     )
            #     self.button[i].pack()
            if (i + 1) % 5 == 0:
                tx = (i + 1) // 5
                butt = ((i + 1) // 5) - 1
                self.button.append(
                    tk.Button(
                        self,
                        text=f"Flashcard Set {tx}",
                        command=lambda i=butt: self.open_this(i),
                    )
                )
                self.button[butt].pack()
                label = tk.Label(self, text=f"Flashcard Media Type: {res[i][8]}")
                label.pack()
                label = tk.Label(self, text=f"Flashcard Content Type: {res[i][10]}")
                label.pack()
                count = count + 1
            # count = count + 1

        def back_click():
            # label1.destroy()
            # label2.destroy()
            # button.destroy()
            # for widget in FlashcardHomePage.winfo_children(self):
            #     widget.destroy()
            # QuizHomePage.pack_forget()
            self.controller.show_frame(HomePage)
            # button3 = ttk.Button(self, text="Back", command=back_click)
            # button3.pack()

        button3 = ttk.Button(self, text="Back", command=back_click)
        button3.pack()

    def open_this(self, myNum):
        # print(myNum)
        global flashCardSetNum
        flashCardSetNum = myNum
        self.controller.show_frame(FlashcardPage)


class FlashcardPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global flashCardSetNum

    def update(self):
        global flashCardSetNum
        one = (flashCardSetNum) * 5
        two = (flashCardSetNum + 1) * 5
        sql = f"""
        select * 
        from flashcards join flashcard_content_type
        on flashcards.flashcard_id = flashcard_content_type.flashcard_id
        where flashcards.flashcard_id > {one-1} and flashcards.flashcard_id < {two+1}
        """
        cursor_obj.execute(sql)
        res = cursor_obj.fetchall()
        self.button = []

        def open_this(num):
            messagebox.showinfo(
                "Answer", f"Answer: {res[num][2]}\nExplanation: {res[num][3]}"
            )

        for i in range(len(res)):
            label = ttk.Label(self, text=f"Flashcard {res[i][0]}: ", padding=(0, 15))
            label.pack()
            label = ttk.Label(self, text=f"Flashcard Content Type:  {res[i][0]}: ")
            label.pack()
            label = ttk.Label(self, text=f"Question: {res[i][1]}")
            label.pack()
            self.button.append(
                tk.Button(
                    self,
                    text=f"Answer",
                    command=lambda i=i: open_this(i),
                )
            )
            self.button[i].pack()

        def back_click():
            # label1.destroy()
            # label2.destroy()
            # button.destroy()
            for widget in FlashcardPage.winfo_children(self):
                widget.destroy()
            # QuizHomePage.pack_forget()
            self.controller.show_frame(FlashcardHomePage)

        button3 = ttk.Button(self, text="Back", command=back_click)
        button3.pack()


app = tkinterApp()
app.title = "Education Platform"
# app.geometry("1920x1080")
app.state("zoomed")
app.mainloop()
