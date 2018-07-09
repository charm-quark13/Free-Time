#!/usr/bin/python3
import os
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as BS
from bs4 import SoupStrainer

def pagescrape(initial_html,header,query):
    x = requests.get(initial_html,headers=header)
    webpage = x.content.decode()

    soup = BS(webpage,'lxml')
    if query:
        search_term = eval(input('Input the html tag containing the url strings to be iterated over:\n'))
        for entrant in soup.find_all(str(search_term)):
            iterables = str(entrant).split()
            print(iterables)
            print('Additional descriptors needed to properly define webpage iterations')
    else:
        a=1
        while a==1:
            try:
                iter = eval(input('Enter list of values to be iterated through on webpage:\n'))
                distance = initial_html.find(str(iter[0]))
                for x in iter:
                    total_length = len(str(x))
                    new_html = initial_html[0:distance] + str(x) + initial_html[distance+total_length:]
                    a=0
            except ValueError:
                print('Invalid Entry')
                a=1

#url = 'https://byo.com/resource/hops/?beer-style=american-amber-ale&tax-submit=Submit'
#
#header = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#
#x = requests.get(url,headers=header)
#webpage=x.content.decode()
#
#soup = BS(webpage,'lxml')
#beer_types = []
#for ingredients in soup.find_all('form'):
#    styles = str(ingredients).split()
#    for entries in styles:
#        if str('value=') in entries:
#            q1 = entries.find('"')
#            q2 = entries.rfind('"')
#            beer_types.append(entries[q1+1:q2])
#            #print(entries[q1+1:q2])
#    #print(values)
##print(soup.body.find_all('div',class_='col-xs-12'))
#
#one_type = []
#one_type = beer_types[0]
#
#for beer in beer_types:
#    print(beer)
#    url = 'https://byo.com/resource/hops/?beer-style=' + beer + '&tax-submit=Submit'
#    x = requests.get(url,headers=header)
#    webpage=x.content.decode()
#    soup = BS(webpage,'lxml')
#    with open(str(beer)+'.html','w') as f:
#        f.write(soup.prettify())

#    for tag in soup.find_all('div',class_='col-xs-12 col-md-8 col-lg-9'):
#        n_rows = 0
#        n_columns = 0
#        for table in tag.find_all('div',class_='col-xs-12'):
#            print(table)
#            n_rows += 1
#            print(tag.text.strip())
#        print(n_rows)

#dir_str = '/home/ep3/Desktop/'
#directory = os.fsencode(dir_str)
#
#for file in os.listdir(dir_str):
#    filename = os.fsdecode(file)
#    if filename.endswith('.html'):
#        os.chdir(dir_str)
#        print(filename)
#        with open(filename,'r') as doc:
#            parse = BS(doc,'lxml')
#            for tag in parse.find_all('div',class_='col-xs-12 col-md-8 col-lg-9'):
#                n_rows = 0
#                n_columns = 0
#                for row in tag.find_all('div',class_='row'):
#                    n_rows += 1
#                    print(tag.text.strip())
#                print(n_rows)
            #a = [x.extract() for x in parse(attrs={'class':'col-xs-3'})]
            #print(parse.body.find_all(attrs={'class':'col-xs-2'}))
            #value = a.get_text()
            #value.split
#            current = parse.body.find_all(attrs={'class':'col-xs-2'})
#            print(current)
#            continue

initial_html = eval(input('Provide intial website url wanting to parse:\n'))
header = eval(input('Provide header for website access:\n'))
z=0
while z == 0:
    try:
        raw_query = eval(input('Will a list need to be created from the intial website that be iterated over? \n'))
        test_query = raw_query.lower()
        if test_query == 'yes':
            test_query = True
            z=1
        elif test_query == 'no':
            test_query = False
            z=1
    except ValueError:
        print('Please answer yes or no.')
        z=0

pagescrape(initial_html,header,query)

#parse = BS(doc)
#print(parse.body.find('div',class_="col-xs-12 col-md-6 col-lg-4"))
