# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 15:58:29 2022

@author: 唐琪登
"""

import pandas as pd

car = pd.read_csv('joyful_pandas_dataset/car.csv')
c_car = car.groupby('Country')

