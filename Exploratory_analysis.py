import pandas as pd 
import numpy as np
df = pd.read_csv('airbnb.csv')
#we can first load and view the data
df.head()

#check for missing data
missing_data = df.isnull()
missing_data.head()

#check per column for the whole data set
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print('')

df.dtypes
#check total number of each neighbourhoood_group
df['neighbourhood_group'].value_counts()
  
#Label encoding for room type
#create dummies a and b
#a is for room_type , b is for neighbourhood_group
# dummies will enable alteration of the original csv file
a = pd.get_dummies(df['room_type'])
a.tail()
a.rename(columns ={'room_type':'Entire home/apt','room_type':'Private room','room_type':'Shared room'})
df = pd.concat([df, a], axis =1)
df.head()

b = pd.get_dummies(df['neighbourhood_group'])
b.rename(columns ={'neighbourhood_group':'Manhattan','neighbourhood_group':'Brooklyn',
                   'neighbourhood_group':'Queens','neighbourhood_group':'Bronx',
                   'neighbourhood_group':'Staten Island'}, inplace = True)
df = pd.concat([df, b], axis =1)
df.head()

X = df[['number_of_reviews','minimum_nights','availability_365']]
X[0:5]

#let us stanfdardize because of different data units which have been combined
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit_transform(X)
X[0:5]

#we can group by neighbourhood_group and room_type to see average prices are across each group
df_1 = df[['room_type', 'neighbourhood_group', 'price']]
group = df_1.groupby(['room_type', 'neighbourhood_group'], as_index= False).mean()
group
#we see that average price for an entire home/apt in Manhattan is the most expensive

#arrange the data in a better and more presentable way
pivot = group.pivot(index = 'neighbourhood_group', columns = 'room_type')
pivot

#we can calculate the ANOVA, so as to help us reject the null hypothesis
from scipy import stats
df_a = df[['neighbourhood_group', 'price']]
df_b = df_a.groupby(['neighbourhood_group'])
df_b.get_group('Queens')['price']
f_test_score, p_value = stats.f_oneway(df_b.get_group('Queens')['price'],df_b.get_group('Bronx')['price'],
                                      df_b.get_group('Brooklyn')['price'],df_b.get_group('Staten Island')['price'],
                                       df_b.get_group('Manhattan')['price'])

f_test_score, p_value
#with such a high f_test score, we can confidently say that prices vary largely depending
#on the neighbourhood_group
#same goes for private rooms and shared rooms. Manhattan has generally the highest prices
