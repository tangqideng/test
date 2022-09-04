# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 20:17:52 2022

@author: 唐琪登
"""

#%%
import pandas as pd

source_A = pd.read_csv("amazon-google/tableA.csv", index_col='id')
sample = source_A.head(5)
source_B = pd.read_csv('amazon-google/tableB.csv', index_col='id')
train = pd.read_csv('amazon-google/train.csv')
df = pd.read_csv('learn_pandas.csv')

df_demo = df[['Name', 'Gender']]
df_demo.drop_duplicates()

#%% replace
df_demo = df_demo.replace(['Female','Male'],[0,1])
source_A['price'] = source_A['price'].fillna(value=0)
source_A['price'].clip(0,100)
# mask and where 替换的是相反的，mask替换True，where替换False

#%% 排序
df_demo = df[['Grade', 'Name', 'Height',
            'Weight']].set_index(['Grade','Name'])


df_demo.sort_values('Height', inplace=True)

#多列排序
df_demo.sort_values(['Weight','Height'],ascending=[True,False],
                    inplace=True)

#%% 行迭代、列迭代
import numpy as np
def sqrt(price):
    if price < 100:
        pass
    else:
        price = np.sqrt(price)
    return price

new_price = source_A['price'].apply(sqrt)

#%% assert
import numpy as np
def plus(v_1,v_2):
    assert len(v_1) == len(v_2)
    return v_1 + v_2

value = plus(np.random.randint(1,5,2), np.random.randint(1,5,3))
print(value)


