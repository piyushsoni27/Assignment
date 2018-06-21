#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 17:59:46 2018

@author: piyush
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import numpy as np

salesperson_df = pd.read_excel("African Mobile Data.xlsx", sheetname="SalespersonData")
sales_df = pd.read_excel("African Mobile Data.xlsx", sheetname="SalesData")

"""
fig, ax = plt.subplots(figsize=(10,8))
groups.get_group("Western").plot("Sales", "Profit",marker='o', linestyle="")
plt.show()

groups = sales_df.groupby("Region")

for name, group in groups:
    ax.plot(group.Sales, group.Profit, marker="o", linestyle="", label=name, alpha=0.6)

ax.legend()

plt.show()


## Sales by Region
sns.pairplot(x_vars="Sales", y_vars="Profit", hue="Region", data=sales_df, size=10, 
             kind='reg',plot_kws=dict(fit_reg=False, scatter_kws=dict(alpha=0.7)))

"""

def plot_(df, ax):
    groups = df.groupby("Country")

    for i, (name, group) in enumerate(groups):
        c = cm.hot(i/5.,1)
        x=group.Sales
        y=group.Profit
        ax.plot(group.Sales, group.Profit, marker="o", linestyle="", label=name, alpha=0.4, color=c)
        ax.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color=c, alpha=0.8)
    
    ax.legend()
    
    return

## Sales by Country
groups = sales_df.groupby("Region")

western_group = groups.get_group("Western")
eastern_group = groups.get_group("Eastern")
middle_group = groups.get_group("Middle")
southern_group = groups.get_group("Southern")
northern_group = groups.get_group("Northern")

#groups.get_group("Western").plot("Sales", "Profit",marker='o', linestyle="")

fig, big_axes = plt.subplots( figsize=(15.0, 15.0) , nrows=5, ncols=1, sharey=True) 

for (row, big_ax), (name, group) in zip(enumerate(big_axes), groups):
    
    big_ax.set_title("Region %s \n" % name, fontsize=16)
    
    # Turn off axis lines and ticks of the big subplot 
    # obs alpha is 0 in RGBA string!
    big_ax.tick_params(labelcolor=(1.,1.,1., 0.0), top='off', bottom='off', left='off', right='off')
    # removes the white frame
    big_ax._frameon = False

j=1;
for i in range(0,3):
    ax = fig.add_subplot(5,3,j)
    ax.set_title('Plot title ' + str(j))
    j+=1
    if(i<2):
        plot_(eastern_group.loc[eastern_group.Country.isin(eastern_group.Country.unique()[i*5:(i+1)*5])], ax)
        #eastern_group.loc[eastern_group.Country.isin(eastern_group.Country.unique()[i*5:(i+1)*5])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
    else:
        plot_(eastern_group.loc[eastern_group.Country.isin(eastern_group.Country.unique()[i*5:])], ax)
        #eastern_group.loc[eastern_group.Country.isin(eastern_group.Country.unique()[i*5:])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
    
for i in range(0,3):
    ax = fig.add_subplot(5,3,j)
    ax.set_title('Plot title ' + str(j))
    j+=1
    if(i<2):
        plot_(middle_group.loc[middle_group.Country.isin(middle_group.Country.unique()[i*3:(i+1)*3])], ax)
        #middle_group.loc[eastern_group.Country.isin(middle_group.Country.unique()[i*3:(i+1)*3])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
    else:
        plot_(middle_group.loc[middle_group.Country.isin(middle_group.Country.unique()[i*3:])], ax)
       # middle_group.loc[eastern_group.Country.isin(middle_group.Country.unique()[i*3:])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
  
for i in range(0,3):
    ax = fig.add_subplot(5,3,j)
    ax.set_title('Plot title ' + str(j))
    j+=1
    if(i<2):
        plot_(northern_group.loc[northern_group.Country.isin(northern_group.Country.unique()[i*2:(i+1)*2])], ax)
        #northern_group.loc[northern_group.Country.isin(northern_group.Country.unique()[i*2:(i+1)*2])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
    else:
        plot_(northern_group.loc[northern_group.Country.isin(northern_group.Country.unique()[i*2:])], ax)
        #northern_group.loc[northern_group.Country.isin(northern_group.Country.unique()[i*2:])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
  
for i in range(0,3):
    ax = fig.add_subplot(5,3,j)
    ax.set_title('Plot title ' + str(j))
    j+=1
    if(i<2):
        plot_(southern_group.loc[southern_group.Country.isin(southern_group.Country.unique()[i*2:(i+1)*2])], ax)
        #southern_group.loc[southern_group.Country.isin(southern_group.Country.unique()[i*2:(i+1)*2])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
    else:
        plot_(southern_group.loc[southern_group.Country.isin(southern_group.Country.unique()[i*2:])], ax)
        #southern_group.loc[southern_group.Country.isin(southern_group.Country.unique()[i*2:])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
  
for i in range(0,3):
    ax = fig.add_subplot(5,3,j)
    ax.set_title('Plot title ' + str(j))
    j+=1
    if(i<2):
        plot_(western_group.loc[western_group.Country.isin(western_group.Country.unique()[i*5:(i+1)*5])], ax)
        #western_group.loc[western_group.Country.isin(western_group.Country.unique()[i*5:(i+1)*5])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
    else:
        plot_(western_group.loc[western_group.Country.isin(western_group.Country.unique()[i*5:])], ax)
        #western_group.loc[western_group.Country.isin(western_group.Country.unique()[i*5:])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
      
fig.set_facecolor('w')
plt.tight_layout()
plt.show()