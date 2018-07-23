# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 22:06:04 2018

@author: E015919
"""

# import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import seaborn as sns

#try 2017 Q3 data first to do the exploratory analysis.
data2017q3 = pd.read_csv('C:\\Users\\E015919\\Downloads\\bikesharedata\\2017-3rd-quarter.csv')
data2017q3.info()
print(data2017q3.head())
# Success
print("Capital Bikeshare dataset 2017 Q3 has {} data points with {} variables each.".format(*data.shape))

data2017q3.describe()

# convert Start Date and End Date columns data into datetime data type
data2017q3['Start date'] = pd.to_datetime(data2017q3['Start date'], format='%Y-%m-%d %H:%M')
data2017q3['End date'] = pd.to_datetime(data2017q3['End date'], format='%Y-%m-%d %H:%M')
data2017q3.info()

data2017q3['Route'] = data2017q3['Start station'] + " to " + data2017q3['End station']
#number of rides by route
routes = data2017q3.groupby('Route')['Member type'].count()
routes_Reg = data2017q3[data2017q3['Member type'] == 'Member'].groupby('Route')['Member type'].count()
routes_Cas = data2017q3[data2017q3['Member type'] == 'Casual'].groupby('Route')['Member type'].count()

most_pop_route = data2017q3['Route'].mode().to_string(index = False)
    print('The most popular route is {}.'.format(most_pop_route))
#The most popular route is Lincoln Memorial to Jefferson Memorial.

routes.describe()
##List top 10 routes in 2017 q3 (bar chart)

temp = routes.reset_index()
top10=temp.sort_values(['Member type'], ascending = False).head(10)
top10.plot.bar(x="Route", y="Member type",legend= False)
plt.title('10 Most Popular Routes: 2017 Q3')

##List top 10 routes in 2017 q3, for registered members only (bar chart)
temp1=routes_Reg.reset_index()
top10_Reg=temp1.sort_values(['Member type'], ascending = False).head(10)
top10_Reg.plot.bar(x="Route", y="Member type",legend=False)
plt.title('10 Most Popular Routes for Regular Members: 2017 Q3')

##List top 10 routes in 2017 q3, for casual members only (bar chart)
temp2=routes_Cas.reset_index()
top10_Cas=temp2.sort_values(['Member type'], ascending = False).head(10)
top10_Cas.plot.bar(x="Route", y="Member type",legend=False)
plt.title('10 Most Popular Routes for Casual Users: 2017 Q3')

#Create day of week; hour
data2017q3['weekday'] = data2017q3['Start date'].apply(lambda x: x.weekday())
data2017q3['hour'] = data2017q3['Start date'].apply(lambda x: x.hour)

# Bike trip by hour for Casual users
tripbyhr=data2017q3[data2017q3['Member type']== 'Casual'].groupby(['hour'])['Member type'].count()
temp3 = tripbyhr.reset_index()
temp3.plot.bar(x="hour", y="Member type",legend= False)
plt.title('Bike use by hour for Casual Users')
# Bike trip by hour for Regular members
tripbyhr2=data2017q3[data2017q3['Member type']=='Member'].groupby(['hour'])['Member type'].count()
tem4 = tripbyhr2.reset_index()
tem4.plot.bar(x="hour", y="Member type",legend= False)
plt.title('Bike use by hour for Regular Members')
##