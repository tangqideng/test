# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 09:19:00 2022

@author: 唐琪登
"""

#%%
import pandas as pd
import numpy as np

df = pd.read_csv('joyful_pandas_dataset/learn_pandas.csv')
group = df.groupby('Gender')['Height'].mean()

# 按多个属性分组
mul_group = df.groupby(['School', 'Gender'])['Height'].mean()

# 按条件分组
condition = df.Weight > df.Weight.mean()
df.groupby(condition)['Height'].mean()

# 按上下四分位数分组
condition_1 = df.Weight <= df.Weight.quantile(0.25)
conditioon_2 = (df.Weight.quantile(0.25) < df.Weight) & (df.Weight <= df.Weight.quantile(0.75))
conditioon_3 = df.Weight > df.Weight.quantile(0.75)

con_value = df.groupby([condition_1, conditioon_2, conditioon_3])['Height']
con_value.describe()

#%% 
item = np.random.choice(list('abc'), df.shape[0])
new_group = df.groupby(item)['Height']

# 获取某一个组
b_group = df.groupby(item)['Height'].get_group('b')

# groupby对象
gb = df.groupby(['School','Grade'])
gb.ngroups
res = gb.groups
group_number = res.keys() # 返回一个的是一个可以迭代的对象

gb.size()

#
mean_value = df[['Height','Weight']].apply(lambda x: x.mean(), axis=0)

# 气象数据集
qixiang_data = pd.read_csv('joyful_pandas_dataset/附件2-行业日负荷数据.csv')
groups = qixiang_data.groupby('Type')
a,b,c,d = groups.groups
group_a = groups.get_group(a)

#%% agg方法，聚合方法
gb = df.groupby('School')[['Height','Weight']]
result = gb.agg(lambda x: x.mean() - x.min())

gb.transform(lambda x: x.mean())



