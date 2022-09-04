# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 11:56:38 2022

@author: 唐琪登
"""

#%% 第二章 EX1：
import pandas as pd

pokemon = pd.read_csv('joyful_pandas_dataset/pokemon.csv').drop(columns='id')

def test_1(line):
    index = line.index
    HP, Attack, Defense, Sp_Atk, Sp_Def, Speed = index[4:]
    total = index[3] 
    return line[HP] + line[Attack] + line[Defense] + \
        line[Sp_Atk] + line[Sp_Def] + line[Speed] == line[total]


result_1 = pokemon.apply(test_1, axis=1)

result_1.value_counts()

types_1_2 = pokemon[['Type 1','Type 2']].value_counts()
sp_attack = pokemon['Sp. Atk']
sp_attack = sp_attack.mask(sp_attack>120, 'high')

upper_type_1 = pokemon['Type 1'].replace({i:i.upper() for i in pokemon['Type 1'].unique()})
upper_type_1_apply = pokemon['Type 1'].apply(lambda x:x.upper())
(upper_type_1 == upper_type_1_apply).all()

import numpy as np
pokemon['deviation'] = pokemon[pokemon.columns[4:]].apply(lambda x:np.max((x-x.mean()).abs()), 
                                                          axis = 1)

#%% 指数加权窗口
s = pd.Series(np.arange(30).cumsum())

def ewm_func(x, alpha=0.2):
    win = (1-alpha)**np.arange(x.shape[0])[::-1]
    res = (win*x).sum()/win.sum()
    return res


s.expanding().apply(ewm_func).head()

#%% 行索引器

