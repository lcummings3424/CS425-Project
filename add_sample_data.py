import psycopg2

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
# "postgres://nh_lc_educationplatform_user:ctX1mTYO5izqzBT38CShz4ZknhCeUmA4@dpg-clprccbd3o9c73evjtlg-a.ohio-postgres.render.com/nh_lc_educationplatform?ssl=true"
# "postgres://nh_lc_educationplatform_user:ctX1mTYO5izqzBT38CShz4ZknhCeUmA4@dpg-clprccbd3o9c73evjtlg-a.ohio-postgres.render.com/nh_lc_educationplatform"
cursor_obj = con.cursor()
sql_file = open("Sample_data.sql", "r")
cursor_obj.execute(sql_file.read())
con.commit()
