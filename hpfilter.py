# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:44:39 2015

@author: Днс
"""
#Ipmort nessesaru packages
import numpy as np
import scipy as sp
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd 


# Ask for a data series and parameters


# Generate artificial data (2 regressors + constant) to test
nobs = 100
X = np.random.random((nobs, 1))
X_name = 'GDP'
times = pd.date_range('1980', periods=nobs, freq='A')

# HP Filter
lambda_hp = 1600
hp_cycle, hp_trend = sm.tsa.filters.hpfilter(X,lambda_hp)

#First and second differences
diff = np.diff(X,axis=0)
diff2 = np.diff(X,2,axis=0)

#Band-pass
band_pass = sm.tsa.filters.bkfilter(X, low=6, high=24, K=12)

#Plot all series
def plot_series(X,hp_trend, hp_cycle, lambda_hp, diff, band_pass):
    figure = plt.figure()

    # Raw data         
    plot_raw = figure.add_subplot(3,2,1)
    plot_raw.plot(times,X)
    plot_raw.set_title('Raw Data '+ X_name)
    


    # HP-Filter    
    plot_hp = figure.add_subplot(3,2,3)
    plot_hp.plot(times,X)
    plot_hp.plot(times,hp_trend, 'r')
    plot_hp.set_title('HP-Filter Trend, lambda= '+str(lambda_hp))
    #plot_hp.set_title(r'$\sigma_i=15$')
    plot_hp2 = figure.add_subplot(3,2,4)
    plot_hp2.plot(hp_cycle, 'g')
    plot_hp2.set_title('HP-Filter Cycle')
    
    # First differences   
    plot_diff = figure.add_subplot(3,2,5)
    plot_diff.plot(diff, 'g')
    plot_diff.set_title('First Differences')
    
    
    #Second differences   
    plot_diff2 = figure.add_subplot(3,2,6)
    plot_diff2.plot(diff2, 'g')
    plot_diff2.set_title('Second Differences')

    # Band-Pass Filter    
    plot_bp = figure.add_subplot(3,2,2)
    plot_bp.plot(band_pass, 'g')
    plot_bp.set_title('Band-Pass Filter ')
    
    plt.tight_layout()    
    return figure
    
final_plot = plot_series(X,hp_trend, hp_cycle, lambda_hp, diff, band_pass)
final_plot.show()
