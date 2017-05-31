'''
Created on May 26, 2017

@author: makaidaimyo
'''

import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def drop_table(tb_name):
    try:
        c.execute("DROP TABLE " + tb_name)
    except Exception as e:
        print(e)

def create_table(tb_name):
    try:
        c.execute("CREATE TABLE " + tb_name + "(language VARCHAR, version REAL, skill TEXT)")
    except Exception as e:
        print(e)

def enter_data(language, version, skill):
    c.execute("INSERT INTO example (language, version, skill) VALUES (?,?,?)", (language, version, skill))
    conn.commit()

def read_data(sql, sql_filter):
    for row in c.execute(sql, [sql_filter]):
        print(row) 
    
        
        
#drop_table('example')
create_table('example')
enter_data('Python', '2.7','Beginner')
enter_data('Python', '3.3','Intermediate')
enter_data('Python', '2.4','beginner')

read_data("SELECT * FROM example WHERE upper(Skill) == upper(?)", 'beginner')
conn.close()


