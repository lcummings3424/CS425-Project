import psycopg2

con = psycopg2.connect(
    database="EducationPlatform",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
)
# con = psycopg2.connect(
#     "postgres://nh_lc_educationplatform_user:ctX1mTYO5izqzBT38CShz4ZknhCeUmA4@dpg-clprccbd3o9c73evjtlg-a.ohio-postgres.render.com/nh_lc_educationplatform"
# )
# "postgres://nh_lc_educationplatform_user:ctX1mTYO5izqzBT38CShz4ZknhCeUmA4@dpg-clprccbd3o9c73evjtlg-a.ohio-postgres.render.com/nh_lc_educationplatform?ssl=true"
# "postgres://nh_lc_educationplatform_user:ctX1mTYO5izqzBT38CShz4ZknhCeUmA4@dpg-clprccbd3o9c73evjtlg-a.ohio-postgres.render.com/nh_lc_educationplatform"
cursor_obj = con.cursor()
sql_file = open("Sample_data.sql", "r")

# sql = """
# INSERT INTO
#     flashcards (
#         flashcard_id,
#         question,
#         answer,
#         answer_explanation
#     )
# VALUES

# """
# cursor_obj.execute(sql_file.read())
# con.commit()
from tkinter import messagebox

messagebox.showerror(
    "ERROR",
    "This file is not needed. All data is already hosted to the database. Uncomment lines 29 and 30 to commit the sample data file to the local host if that is what you desire. Otherwise, you can run either the executable or education_platform.py file as is.",
)
