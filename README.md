# CS425-Project

This project makes a few assumptions:

- You have postgresql installed on your system
- You have the admin username set up as "postgres"
- You have the admin passwoed set up as "posgres"
- You have the Schema.sql file hosted on your system (localhost) with the name "Education Platform". On my system, i use [Postbird](https://github.com/Paxa/postbird) for importing the sql file and setting up the database
- The database is hosted on port 5432
- You have run "add_sample_data.py"

It will not work if these items have not been completed (in that order).
If all of this has been completed, you can launch the executable located in \dist\education_platform
The executable will not work if it is not in the same folder as all files contained in \dist\education_platform (i.e. must be kept in the same structure as it is in the repository)
