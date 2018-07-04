#!/usr/bin/python3
import os
from bs4 import BeautifulSoup as BS
from bs4 import SoupStrainer


dir_str = '/home/ep3/Desktop/'
directory = os.fsencode(dir_str)

for file in os.listdir(dir_str):
    filename = os.fsdecode(file)
    if filename.endswith('.html'):
        os.chdir(dir_str)
        print(filename)
        with open(filename,'r') as doc:
            parse = BS(doc,'lxml')
            value = parse.get_text()
            a = [x.extract() for x in parse(attrs={'class':'col-xs-3'})]
            #print(parse.body.find_all(attrs={'class':'col-xs-2'}))
            #value = a.get_text()

            for m in a:
                print(str(m).split())

#            current = parse.body.find_all(attrs={'class':'col-xs-2'})
#            print(current)
            continue





#parse = BS(doc)
#print(parse.body.find('div',class_="col-xs-12 col-md-6 col-lg-4"))
