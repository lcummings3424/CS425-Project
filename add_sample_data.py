import psycopg2

con = psycopg2.connect(
    database="test",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
)
cursor_obj = con.cursor()
sql_file = open("Sample_data.sql", "r")
cursor_obj.execute(sql_file.read())
con.commit()