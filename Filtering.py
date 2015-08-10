# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:44:39 2015

@author: Днс
"""
#Ipmort nessesaru packages
import numpy as np
#import scipy as sp
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd 
from tkinter import *
#import tkinter
from tkinter.filedialog import askopenfilename

# Ask for a data series and parameters
fields = ('Choose Data', 'Starting date')

#get variables entries(1) and entries (2)
def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"")
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries

#self.vars(1), self.vars(2)...
class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
        return map((lambda var: var.get()), self.vars)


 #  def allstates(): 
 #     print(list(lng.state()), list(tgl.state()))
def enter_file():
    Tk().withdraw()
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    #return open (filename, 'r')
    return filename
    #return open(filename, 'r')

if __name__ == '__main__':
   root = Tk()
   Label(root, text="Quick Data Filtering with Standard Parameters").pack()
 #  button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}   
 #  Tkinter.Button(self, text='askopenfilename', command=self.askopenfilename).pack(**button_opt) 

   b0 = Button(root, text='Choose Data File', command=enter_file)   
   b0.pack(side=RIGHT, padx=5, pady=2)
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   freq = Checkbar(root, ['Quarterly', 'Annual'])
   filt = Checkbar(root, ['HP','Band-Pass', 'First Differences'])
   filt.pack(side=TOP,  fill=X)
   freq.pack(side=LEFT)
   filt.config(relief=GROOVE, bd=2)  
   b1 = Button(root, text='Run',
          command=(lambda e=ents: final_balance(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
   
        
#Open the data file
X =[]
#data_file = open('filename', 'r')
use_file = data_file.read().split('\n')
data_file.close

#Read data X from the file
for x in use_file:
    element = x.split('\n')
    X.append(int[element])
      

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
