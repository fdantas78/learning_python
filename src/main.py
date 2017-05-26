'''
Created on May 24, 2017

@author: makaidaimyo

Python Web Programming
'''

import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table(tb_name):
    try:
        c.execute("CREATE TABLE " + tb_name + "(language VARCHAR, version REAL, skill TEXT)")
    except Exception as e:
        print(e)

def enter_data(language, version, skill):
    c.execute("INSERT INTO example (language, version, skill) VALUES (?,?,?)", (language, version, skill))
       
    conn.commit()
        
        

create_table('example')
enter_data('Python', '2.7','Begginner')
enter_data('Python', '3.3','Intermediate')
enter_data('Python', '2.4','Begginner')
conn.close()


