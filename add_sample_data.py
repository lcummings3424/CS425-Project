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
# (
#     6,
#     'What is the primary key used for in a database table?',
#     'Uniquely identifies each record',
#     'The primary key is used to uniquely identify each record in a database table.'
# ),
# (
#     7,
#     'What is the difference between INNER JOIN and LEFT JOIN in SQL?',
#     'INNER JOIN returns matching rows, LEFT JOIN returns all rows from the left table and the matching rows from the right table',
#     'INNER JOIN returns only the rows that have matching values in both tables, while LEFT JOIN returns all rows from the left table and the matching rows from the right table.'
# ),
# (
#     8,
#     'Explain the purpose of the WHERE clause in a SQL query.',
#     'Filters rows based on a specified condition',
#     'The WHERE clause is used to filter rows in a SQL query based on a specified condition.'
# ),
# (
#     9,
#     'What is normalization in database design?',
#     'Organizing data to reduce redundancy and improve data integrity',
#     'Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity.'
# ),
# (
#     10,
#     'What is an index in a database?',
#     'Improves the speed of data retrieval operations on a database table',
#     'An index in a database is a data structure that improves the speed of data retrieval operations on a database table.'
# );

# """
# cursor_obj.execute(sql_file.read())
# cursor_obj.execute(sql)
# con.commit()
from tkinter import messagebox

messagebox.showerror(
    "ERROR",
    "This file is not needed. All data is already hosted to the database. Uncomment lines 59, 60, and 61 to commit the sample data file to the local host if that is what you desire. Otherwise, you can run either the executable or education_platform.py file as is.",
)
