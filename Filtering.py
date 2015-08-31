# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:44:39 2015

@author: Днс

"""

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.filedialog import askopenfilename
from numpy import *


def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field + ": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries


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


def enter_file(entries):
    Tk().withdraw()
    # show an "Open" dialog box and return the path to the selected file
    filename = askopenfilename()
    entries['Data File'].delete(0, END)
    entries['Data File'].insert(0, filename)
    return filename


def plot_series(X, X_name, time, hp_trend, hp_cycle, lambda_hp, X_hp, diff, diff2, band_pass):
    figure = plt.figure()
    figure.suptitle(X_name)
    # Raw data
    plot_raw = figure.add_subplot(3, 2, 1)
    plot_raw.plot(time, X)
    plot_raw.set_title('Raw Data ' + X_name)
    # HP-Filter
    plot_hp = figure.add_subplot(3, 2, 3)
    plot_hp.plot(X_hp)
    plot_hp.plot(hp_trend, 'r')
    plot_hp.set_title('HP-Filter Trend, lambda= ' + str(lambda_hp))
    plot_hp.set_xticklabels([])
    # plot_hp.set_title(r'$\sigma_i=15$')
    plot_hp2 = figure.add_subplot(3, 2, 4)
    plot_hp2.plot(hp_cycle, 'g')
    plot_hp2.set_title('HP-Filter Cycle')
    plot_hp2.set_xticklabels([])
    # First differences
    plot_diff = figure.add_subplot(3, 2, 5)
    plot_diff.plot(diff, 'g')
    plot_diff.set_title('First Differences')
    plot_diff.set_xticklabels([])
    # Second differences
    plot_diff2 = figure.add_subplot(3, 2, 6)
    plot_diff2.plot(diff2, 'g')
    plot_diff2.set_title('Second Differences')
    plot_diff2.set_xticklabels([])
    # Band-Pass Filter
    plot_bp = figure.add_subplot(3, 2, 2)
    plot_bp.plot(band_pass, 'g')
    plot_bp.set_title('Band-Pass Filter ')
    plot_bp.set_xticklabels([])

    plt.tight_layout()
    return figure


def run(entries):
    # Name of the series:
    X_name = entries['Variable Name'].get()
    filename = str(entries['Data File'].get())
    # Open the data file (the file must be closed)
    time, X = loadtxt(filename, unpack=True)
    filters = list(filt.state())

    # HP Filter
    frequency = list(freq.state())
    quarterly = frequency[0]
    if quarterly == 1:
        lambda_hp = 1600
    else:
        lambda_hp = 6.25
    if filters[0] != 0:
        hp_cycle, hp_trend = sm.tsa.filters.hpfilter(X, lambda_hp)
        X_hp = X
    else:
        hp_cycle = 0
        hp_trend = 0
        X_hp = 0

    # First and second differences
    if filters[1] != 0:
        diff = np.diff(X, axis=0)
        diff2 = np.diff(X, 2, axis=0)
    else:
        diff = 0
        diff2 = 0

    # Band-pass
    if filters[2] != 0:
        band_pass = sm.tsa.filters.bkfilter(X, low=6, high=24, K=12)
    else:
        band_pass = 0

    # Plot all series
    final_plot = plot_series(
        X, X_name, time, hp_trend, hp_cycle, lambda_hp, X_hp, diff, diff2, band_pass)
    final_plot.show()


if __name__ == '__main__':
    root = Tk()
    Label(root, text="Quick Data Filtering with Standard Parameters").pack()
    ents = makeform(root, fields=('Variable Name', 'Data File'))
    b0 = Button(root, text='Choose Data File', command=(lambda e=ents: enter_file(e)))
    b0.pack(side=TOP, padx=5, pady=5)
    freq = Checkbar(root, ['Quarterly', 'Annual'])
    filt = Checkbar(root, ['HP', 'First Differences', 'Band-Pass'])
    filt.pack(side=TOP, fill=X)
    freq.pack(side=LEFT)
    filt.config(relief=GROOVE, bd=2)
    b1 = Button(root, text='Run', command=(lambda e=ents: run(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Quit', command=root.destroy)
    b2.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(root, text='Show', command=root.quit)
    root.mainloop()
