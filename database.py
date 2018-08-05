import sqlite3

class Database:

    conn = sqlite3.connect('signup.db')

    c = conn.cursor()

    #c.execute("""CREATE TABLE signup (
    #   first text,
    #   last text,
    #   email text
    #   )""")

    #c.execute("INSERT INTO signup VALUES ('stephen', 'mugisa', 'smugisa@company.com')")

    #c.execute("SELECT * FROM signup WHERE last='mugisa'")

    #print(c.fetchone())

    conn.commit()
    conn.close()