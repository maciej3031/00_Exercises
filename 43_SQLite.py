import sqlite3
import time
import random
random.seed()

con = sqlite3.connect("dane.db")
c = con.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS tabela (id INTEGER PRIMARY KEY ASC, nrrej TEXT, date1 TEXT)')

def data_entry():
    c.execute("INSERT INTO tabela VALUES(NULL,'WX82981', '2016-01-01')")
    con.commit()

def insert_record_to_db(nrrej = None):
    date1 = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    c.execute("INSERT INTO tabela (id, nrrej, date1) VALUES (NULL ,?, ?)", (nrrej, date1))
    con.commit()

def read_record_from_db(nrrej = None):
    c.execute("SELECT nrrej, date1 FROM tabela WHERE nrrej = ?", (nrrej,))
    data = c.fetchall()
    print(data)
    # for row in c.fetchall():
    #     print(row)

def update_record_in_db():
    c.execute("UPDATE tabela SET nrrej = ? WHERE nrrej = ? ", ("QQ12234", "PP89712"))
    con.commit()

def delete_record_in_db():
    c.execute("DELETE FROM tabela WHERE nrrej = ?", ("QQ12234", ))
    con.commit()

create_table()

# insert_record_to_db("WX82981")

read_record_from_db("WX82981")

# update_record_in_db()

# delete_record_in_db()


c.close()
con.close()
