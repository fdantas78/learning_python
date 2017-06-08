'''
Created on May 31, 2017

@author: makaidaimyo


Python Web Programming
'''

'''
import urllib.request as url_req
import urllib.parse as url_par

url = 'https://www.google.com/search?'
values = {'q':'python programming tutorials'}
data = url_par.urlencode(values)
#data = data.encode('utf_8')

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"

req = url_req.Request(url+data, headers=headers)
resp = url_req.urlopen(req)
resp_data = resp.read()


print(resp_data)

'''

from bs4 import BeautifulSoup as BSoup
import urllib.request as url_req
import time

req = url_req.urlopen('https://www.engadget.com/rss.xml')

xml = BSoup(req, 'xml')

for item in xml.findAll('item'):
    print(item.title)
    print(item.link)
    
    news = url_req.urlopen(item.link.text).read()
    page = BSoup(news, 'lxml')
    for p in page.findAll('p'):
        print(p.text + "\n")
    time.sleep(2)
                

    
    
