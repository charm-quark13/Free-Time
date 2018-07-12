import os
import pandas as pd
import numpy as np

def dfread(filename):
    df = pd.read_csv(str(filename))
    return df

def filefind(filename):
    filepath = str(os.getcwd()) + '/'
    direction = filepath + str(filename)
    return direction

def Pos_Org(dframe):
    d_data = dframe.groupby('Pos').get_group('D')
    sel_data = []
    for position in ['LW','RW','C']:
        sel_data.append(dframe.groupby('Pos').get_group(position))
    f_data = pd.concat(sel_data)
    return f_data, d_data

filename = filefind('skaters-2009.csv')
df = dfread(filename)

filename = filefind('skaters-adv-2009.csv')
adv_df = dfread(filename)

#  Need to get rid of duplicate rows in f_df and d_df before concatenating
#  with the advanced statistics tables.
df = df.drop_duplicates(subset = ['Player','Pos'],keep = 'first')
df = df.reset_index(drop=True)
df = df.drop('Unnamed: 0',axis=1)
adv_df = adv_df.drop('Unnamed: 0',axis=1)

df = df.set_index('Player',drop=False)
adv_df = adv_df.set_index('Player',drop=False)

adf_df, add_df = Pos_Org(adv_df)
f_df, d_df = Pos_Org(df)

f_df = pd.concat([f_df,adf_df],axis=1)
d_df = pd.concat([d_df,add_df],axis=1)

f_df['Thru%'] = f_df['Thru%'].fillna(0.)
d_df['Thru%'] = d_df['Thru%'].fillna(0.)

for datfs in [f_df,d_df]:
    print(datfs.isnull().any())

#print(adf_df)
#print(add_df)
#print(f_df)
#print(d_df)
