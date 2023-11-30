import psycopg2

con = psycopg2.connect(
    database="EducationPlatform",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
)
cursor_obj = con.cursor()
sql_file = open("Sample_data.sql", "r")
cursor_obj.execute(sql_file.read())
con.commit()
cursor_obj.execute("SELECT * FROM users")
result = cursor_obj.fetchall()
print(result)
