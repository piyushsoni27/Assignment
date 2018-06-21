#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 22:01:30 2018

@author: piyush
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 17:59:46 2018

@author: piyush
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

salesperson_df = pd.read_excel("African Mobile Data.xlsx", sheetname="SalespersonData")
sales_df = pd.read_excel("African Mobile Data.xlsx", sheetname="SalesData")


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
        eastern_group.loc[eastern_group.Country.isin(eastern_group.Country.unique()[i*5:(i+1)*5])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
    else:
        eastern_group.loc[eastern_group.Country.isin(eastern_group.Country.unique()[i*5:])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
    
for i in range(0,3):
    ax = fig.add_subplot(5,3,j)
    ax.set_title('Plot title ' + str(j))
    j+=1
    
    print(i)
    
    if(i<2):
        middle_group.loc[middle_group.Country.isin(middle_group.Country.unique()[i*3:(i+1)*3])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
    else:
        middle_group.loc[middle_group.Country.isin(middle_group.Country.unique()[i*3:])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
  
for i in range(0,3):
    ax = fig.add_subplot(5,3,j)
    ax.set_title('Plot title ' + str(j))
    j+=1
    if(i<2):
        northern_group.loc[northern_group.Country.isin(northern_group.Country.unique()[i*2:(i+1)*2])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
    else:
        northern_group.loc[northern_group.Country.isin(northern_group.Country.unique()[i*2:])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
  
for i in range(0,3):
    ax = fig.add_subplot(5,3,j)
    ax.set_title('Plot title ' + str(j))
    j+=1
    
    if(i<2):
        southern_group.loc[southern_group.Country.isin(southern_group.Country.unique()[i*2:(i+1)*2])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
    else:
        southern_group.loc[southern_group.Country.isin(southern_group.Country.unique()[i*2:])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
  
for i in range(0,3):
    ax = fig.add_subplot(5,3,j)
    ax.set_title('Plot title ' + str(j))
    j+=1
    if(i<2):
        western_group.loc[western_group.Country.isin(western_group.Country.unique()[i*5:(i+1)*5])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
    else:
        western_group.loc[western_group.Country.isin(western_group.Country.unique()[i*5:])].plot("Sales", "Profit",marker='o', linestyle="", ax=ax)
      
fig.set_facecolor('w')
plt.tight_layout()
plt.show()