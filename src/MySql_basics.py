'''
Created on Jun 8, 2017

@author: makaidaimyo
'''
'''
pip3 install lxml
'''
#USE PyDB;
#CREATE TABLE links (time FLOAT(18,2), link VARCHAR(400));

from bs4 import BeautifulSoup as BSoup
import time
import urllib.request as url_req
#import urllib2

from MySqlConn import connection
c, conn = connection('PYTHON_DB')

def create_table(tb_name):
    try:
        c.execute("CREATE TABLE " + tb_name + "(time FLOAT(18,2), link VARCHAR(400))")
    except Exception as e:
        print(e)

def enter_data(link):
    c.execute("INSERT INTO links (time, link) VALUES (%s,%s)", (time.time(), link))
    conn.commit()

create_table('links')

def parse_links():
    req = url_req.urlopen('https://www.engadget.com/rss.xml')
    #req = urllib2.urlopen('https://www.engadget.com/rss.xml')
    xml = BSoup(req, 'xml')
    
    new_items = 0
    
    for item in xml.findAll('item'):
        url = item.link.text    
        #print(url)
        c.execute("SELECT * FROM links WHERE link = %s", (url,))
        rows = c.fetchall()
        if len(rows) == 0:
            enter_data(url)
            print("Inserting a new link")
            new_items += 1
        #else:
        #    print(rows)
        #    print("Link already in the database")
            
    print("%s new itens were inserted" % new_items)
    time.sleep(4)
    
for _ in range(5):
    parse_links()

print("Finished parsing!")
conn.close()
    

