#!/usr/bin/python3
import os
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as BS
from bs4 import SoupStrainer


def scrape(x1,x2,html1,html2):
    iter_list = []
    for x in range(x1,x2):
        iter_list.append(x)

    for iter in iter_list:
        html = str(html1) + str(iter) + str(html2)
        x = requests.get(html,headers=header)
        webpage = x.content.decode()
        soup = BS(webpage,'lxml')
        with open('skaters-' +str(iter)+ '.html','w') as f:
            f.write(soup.prettify())

header = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
html1 = 'https://www.hockey-reference.com/leagues/NHL_'
html2 = '_skaters.html'

scrape(2000,2019,html1,html2)
