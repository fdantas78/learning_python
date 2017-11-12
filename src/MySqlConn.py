'''
Created on Jun 8, 2017

@author: makaidaimyo
'''
import MySQLdb

def connection(db_name):
    conn = MySQLdb.connect(host='localhost',
                         user='root',
                         passwd='euqirotciv04',
                         db=db_name)
    c = conn.cursor()
    
    return c, conn

if __name__ == '__main__':
    c, conn = connection('PyDB')
    print('All worked out!')


