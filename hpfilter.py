# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:44:39 2015

@author: Днс
"""
#Ipmort nessesaru packages
import numpy as np
import scipy
import statsmodels.api as sm
import matplotlib.pyplot as plt


# Ask for a data series and parameters


# Generate artificial data (2 regressors + constant) to test
nobs = 100
X = np.random.random((nobs, 1))
X_name = 'GDP'
#X = sm.add_constant(X)
beta = [1, .1, .5]
#e = np.random.random(nobs)
#y = np.dot(X, beta) + e


# HP Filter
lambda_hp = 1600
hp_cycle, hp_trend = sm.tsa.filters.hpfilter(X,lambda_hp)

#First differences
for i 1:
    X_diff[i=X[i]-X[i-1]


#Band-pass
band_pass = sm.tsa.filters.bkfilter(X, low=6, high=24, K=12)
band_pass_cycle = X-band_pass


#Plot all series
    # Raw data     
    figure = plt.figure()
    plot_raw = figure.add_subplot(3,2,1)
    plot_raw.plot(X)
    plot_raw.set_title('Raw Data '+ X_name)

    # HP-Filter    
    plot_hp = figure.add_subplot(3,2,3)
    plot_hp.plot(X)
    plot_hp.plot(hp_trend, 'r')
    plot_hp.set_title('HP-Filter, lambda= '+str(lambda_hp))
    plot_hp2 = figure.add_subplot(3,2,4)
    plot_hp2.plot(hp_cycle, 'g')
    plot_hp2.set_title('HP Cycle')
    
    # Band-Pass Filter
#    plot_bp = figure.add_subplot(3,2,5)
#    plot_bp.plot(X)
#    plot_bp.plot(X-band_pass, 'r')
#    plot_bp.set_title('BP Filter')
    plot_bp2 = figure.add_subplot(3,2,6)
    plot_bp2.plot(band_pass, 'g')
    plot_bp2.set_title('BP Cycle')
    
#    plot_bp = plt.plot(band_pass)
 #   plt.subplot(224) 
 #   plot_fd = plt.plot(diff)
    plt.show()

plt.plot([-500, 0, 550], [-1000, 0, 550])
plt.show()


#Plot series

Figure_all = plt.figure (1)
plt.subplot(221) 
plot_raw = plot_series(X, 'Unfiltered Series', 'GDP')
plt.subplot(222)
plot_hp = plot_series(hp_cycle, 'HP-Filter', 'GDP')
plt.subplot(223) 
plot_bp = plot_series(band_pass, 'BP-Filter', 'GDP')
plt.subplot(224) 
plot_fd = plot_series(diff, 'First Differences', 'GDP')
Figure_all.show()

x = np.random.random((10, 1))
y = np.random.random((10, 1))
figure_try = plt.figure()
axarr = plt.subplots(2, 2)
axarr[0, 0].plot(x, y)
axarr[0, 0].set_title('Axis [0,0]')
axarr[0, 1].scatter(x, y)
axarr[0, 1].set_title('Axis [0,1]')
axarr[1, 0].plot(x, y ** 2)
axarr[1, 0].set_title('Axis [1,0]')
axarr[1, 1].scatter(x, y ** 2)
axarr[1, 1].set_title('Axis [1,1]')
figure_try.show()


plot_all = plot_series()
plot_all.show()