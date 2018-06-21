#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 23:09:29 2018

@author: piyush
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from ipywidgets import widgets, interactive

salesperson_df = pd.read_excel("African Mobile Data.xlsx", sheetname="SalespersonData")
sales_df = pd.read_excel("African Mobile Data.xlsx", sheetname="SalesData")

def plot_dropdown(city):
    df2 = sales_df.copy()
    df2 = df2.loc[df2.City == city]
    
    ts = df2.Profit
    
    ts.index = df2.Date
    
    plt.plot(ts)
    
    return


# Make a dropdown to select the Area, or "All"
city_list = widgets.Dropdown(
    options = list(sales_df.City.unique()),
    description='City:',
)

interactive(plot_dropdown, city=city_list)

