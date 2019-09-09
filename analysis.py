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
    
