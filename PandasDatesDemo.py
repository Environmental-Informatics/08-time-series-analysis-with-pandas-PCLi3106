#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Pin-Ching Li
This code is creared on 4/8/2020
This code is adapted from
http://earthpy.org/pandas-basics.html 
on 4/8/2020
The task of this code is to analyze time series data by pandas
"""

# import modules for following application
import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel
import matplotlib.pyplot as plt
pd.set_option('display.max_rows',15)

# get dataset from the following http location
# need to be run in the command window of spyder or Linux
#!wget http://www.cpc.ncep.noaa.gov/products/precip/CWlink/daily_ao_index/monthly.ao.index.b50.current.ascii
# load the text file downloaded in previous code
ao = np.loadtxt('monthly.ao.index.b50.current.ascii')
# generate the datetime from 1950 till now with timestep equals to a month
dates = pd.date_range('1950-01', periods=ao.shape[0], freq='M')
# let the datetime (dates) be index 
# and combine with series of value in ao dataframe (the third column)
AO = Series(ao[:,2], index=dates)
# plot the monthly timeseries with time as x axis and value as y axis
AO.plot()
plt.show()

# plot AO value from 1980 to 1990

# get dataset from the following http location by wget
#!wget http://www.cpc.ncep.noaa.gov/products/precip/CWlink/pna/norm.nao.monthly.b5001.current.ascii
# load the dataset downloaded by wget
nao = np.loadtxt('norm.nao.monthly.b5001.current.ascii')
# create datetime index for NAO
dates_nao = pd.date_range('1950-01', periods=nao.shape[0], freq='M')
# create NAO value series with datetime index (monthly)
NAO = Series(nao[:,2], index=dates_nao)

# create a dataframe contains AO and NAO files
aonao = DataFrame({'AO' : AO, 'NAO' : NAO})

# plot the annual median value of AO
AO_mm = AO.resample("A").median()
AO_mm.plot()
plt.show()

# plot the Rolling mean for both AO and NAO 
aonao.rolling(window=12, center=False).mean().plot()
plt.show()