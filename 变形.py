# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 16:43:08 2022

@author: 唐琪登
"""

import pandas as pd
import numpy as np


table_A = pd.read_csv('amazon-google/tableA.csv')
column_A = {i: 'A_'+ i for i in table_A.columns}
table_A.columns = column_A.values()

table_B = pd.read_csv('amazon-google/tableB.csv')
column_B = {i: 'B_'+ i for i in table_B.columns}
table_B.columns = column_B.values()

table_train = pd.read_csv('amazon-google/train.csv')

merge_a = table_train.merge(table_A, left_on='ltable_id', right_on='A_id',
                  how = 'left')

merge_a_b = merge_a.merge(table_B, left_on='rtable_id', right_on='B_id',
                  how = 'left')

drop_columns = list(table_train.columns[:-1]) + ['A_id','B_id'] 
train = merge_a_b.drop(columns=drop_columns)
