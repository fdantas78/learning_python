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
#import urllib.parse as url_par

req = url_req.urlopen('https://www.engadget.com/rss.xml')

xml = BSoup(req, 'xml')

for item in xml.findAll('item'):
    #print(item)
    for title in item.findAll('title'):
        print(title)
        for link in item.findAll('link'):
            print(link.text)
    #url = item.text
    #news = url_req.urlopen(url).read()
    #print(news)
    #print(20*"#")
    
    
