#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 03:51:23 2018

@author: piyush
"""

import difflib
import pandas as pd

village = pd.read_excel("Sample.xlsx", sheetname="Census details")
booth = pd.read_excel("Sample.xlsx", sheetname="Booth details")



