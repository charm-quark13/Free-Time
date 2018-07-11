#!/usr/bin/python3
import os
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as BS
from bs4 import SoupStrainer


dir_str = str(os.getcwd())

for file in os.listdir(dir_str):
    filename = os.fsdecode(file)
    if filename.endswith('.html'):
        if filename.find('goalies')!=-1:
            os.chdir(dir_str)
            print(filename)
            hyphen = filename.find('-')
            period = filename.find('.')
            with open(filename,'r') as doc:
                parse = BS(doc,'lxml')
                column_title = []
                for tag in parse.find_all('th',scope="col"):
                    column_title.append(str(tag.text.strip()))
                    if column_title == []:
                            continue
                for table in parse.find_all('tbody'):
                    n_rows = 0
                    row_point = 0
                    for row in table.find_all('tr'):
                        n_rows += 1

                column_title.pop(0)
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

                with open('goalies-'+ str(filename[hyphen+1:period]) + '.csv','w') as f:
                    df.to_csv(path_or_buf=f)
exit()

#                n_rows = 0
#                n_columns = 0
#                point = 0
#                for titles in tag.find_all('div',class_='heading'):
#                    point += 1
#                    if point == 1:
#                        column_title = []
#                        for columns in titles.find_all('div'):
#                            column_title.append(str(columns.text.strip()))
#                            n_columns += 1
#                        column_title.append('Beer Styles')
#                        column_title.insert(2,'Maximum ' + str(column_title[1]))
#                        column_title[1] = 'Minimum ' + str(column_title[1])
#                        #print(column_title)
#                for row in tag.find_all('div',class_='content'):
#                    point = 1
#                    n_rows += 1
#                    #print(tag.text.strip())
#                if n_rows != 0:
#                    df = pd.DataFrame(index=range(n_rows),columns=column_title)
#                    row_point = 0
#                    for row in tag.find_all('div',class_='content'):
#                        col_point = 0
#                        while col_point <= 5:
#                            cols = str(row.get_text())
#                            data_list = cols.splitlines()
#                            data = []
#                            for line in data_list:
#                                if line.strip() != str(''):
#                                    data.append(line.strip())
#                            if len(data) == 3:
#                                data.insert(2,str(''))
#                            data.append(str(filename)[:-5])
##                            print(data)
#                            if col_point == 0:
#                                df.iat[row_point,col_point] = data[col_point]
#                            elif col_point == 1:
#                                trim = data[1][:-1]
#                                trim = trim.split(str('-'))
#                                df.iat[row_point,col_point] = trim[0]
#                            elif col_point == 2:
#                                trim = data[1][:-1]
#                                trim = trim.split(str('-'))
#                                if len(trim) == 1:
#                                    df.iat[row_point,col_point] = trim[0]
#                                else:
#                                    df.iat[row_point,col_point] = trim[1]
#                            else:
#                                df.iat[row_point,col_point] = data[col_point-1]
#                            col_point +=1
#                        row_point += 1
##                    print(df)
#                    poynt += 1
#                    if poynt == 1:
#                        df1 = df
#                    else:
#                        #df_master = pd.concat([df1,df])
#                        df_master = df1.merge(df,how='outer')
#                        df1 = df_master
#
#            continue
