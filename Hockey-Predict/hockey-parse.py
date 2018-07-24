#!/usr/bin/python3
import os
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as BS
from bs4 import SoupStrainer


dir_str = str(os.getcwd())
def csv_gen(name,ftype):
    for file in os.listdir(dir_str):
        filename = os.fsdecode(file)
        if filename.endswith(str(ftype)):
            if filename.find(str(name))!=-1:
                os.chdir(dir_str)
                print(filename)
                hyphen = filename.rfind('-')
                period = filename.find('.')
                with open(filename,'r') as doc:
                    parse = BS(doc,'lxml')
                    column_title = []
                    for tag in parse.find_all('th',scope="col"):
                        column_title.append(str(tag.text.strip()))
                        if column_title == []:
                            continue

                        if len(column_title)>2:
                            for col in range(len(column_title)-1):
                                if column_title[col] == column_title[-1]:
                                    column_title[-1] = str(column_title[col]) + 'A'
                                    column_title[col] = str(column_title[col]) + 'G'

                    for table in parse.find_all('tbody'):
                        n_rows = 0
                        row_point = 0
                        for row in table.find_all('tr'):
                            n_rows += 1
                    try:
                        column_title.pop(0)
                    except:
                        continue

                    df = pd.DataFrame(index = range(n_rows),columns = column_title)
                    for table in parse.find_all('tbody'):
                        row_point = 0
                        row_data = [[]]
                        for row in table.find_all('tr'):
                            col_point = 0
                            row_set = []
                            for entry in row.find_all('td'):
                                row_set.append(entry.get_text('',strip=True))
                            for it1 in row_set:
                                if it1.find('*') != -1:
                                    row_set[0] = it1[0:it1.find('*')]
                            row_data.append(row_set)
                        row_point += 1

                    sub_list = []
                    it1 = 0
                    for it1 in range(len(row_data)):
                        if row_data[it1] == []:
                            sub_list.append(it1)
                    for x in reversed(sub_list):
                        del row_data[x]
                    df = pd.DataFrame(row_data,columns=column_title)

                    with open(str(name) + str(filename[hyphen+1:period]) + '.csv','w') as f:
                        df.to_csv(path_or_buf=f)

csv_gen('skaters-adv-','.html')
