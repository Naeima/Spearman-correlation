
'''This code calculates the Spearman Rank Correlation Coefficient (Rs). 

to run:
........python  spearman.py

'''

# importing libraries 
import numpy as np
import pandas as pd
import scipy.stats

#  Open and read the data
df=pd.read_csv('master.csv')
#print(df)

x= df['x']
y= df['y']
# Calculating  Spearman's using Scipy for Fertility Rate Vs Unemployment Rate.
result= scipy.stats.spearmanr(x, y)[0]
print(result)
# To interpret test result, check out this link https://www.statstutor.ac.uk/resources/uploaded/spearmans.pdf
