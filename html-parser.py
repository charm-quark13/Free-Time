#!/usr/bin/python3
import os
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as BS
from bs4 import SoupStrainer

url = 'https://byo.com/resource/hops/?beer-style=american-amber-ale&tax-submit=Submit'

header = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

x = requests.get(url,headers=header)
webpage=x.content.decode()

soup = BS(webpage,'lxml')
for ingredients in soup.find_all('form'):
    styles = str(ingredients).split()
    for entries in styles:
        if str('value=') in entries:
            print(entries)
    #print(values)
#print(soup.body.find_all('form'))


dir_str = '/home/ep3/Desktop/'
directory = os.fsencode(dir_str)

for file in os.listdir(dir_str):
    filename = os.fsdecode(file)
    if filename.endswith('.html'):
        os.chdir(dir_str)
        print(filename)
        with open(filename,'r') as doc:
            parse = BS(doc,'lxml')
            for tag in parse.find_all('div',class_='col-xs-12 col-md-8 col-lg-9'):
                n_rows = 0
                n_columns = 0
                for row in tag.find_all('div',class_='row'):
                    n_rows += 1
                    #print(tag.text.strip())
                print(n_rows)
            #a = [x.extract() for x in parse(attrs={'class':'col-xs-3'})]
            #print(parse.body.find_all(attrs={'class':'col-xs-2'}))
            #value = a.get_text()
            #value.split
#            current = parse.body.find_all(attrs={'class':'col-xs-2'})
#            print(current)
            continue





#parse = BS(doc)
#print(parse.body.find('div',class_="col-xs-12 col-md-6 col-lg-4"))
