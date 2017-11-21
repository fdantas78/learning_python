'''
Created on Jun 8, 2017

@author: makaidaimyo
'''
'''
sudo apt-get install python-mysqldb
pip3 install pycrypto
'''

import MySQLdb

def connection(db_name):
    conn = MySQLdb.connect(host='localhost',
                         user='root',
                         passwd='',
                         db=db_name)
    c = conn.cursor()
    
    return c, conn

if __name__ == '__main__':
    c, conn = connection('PYTHON_DB')
    print('All worked out!')


