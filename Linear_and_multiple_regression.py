#First, without training and testing data
#simple linear regression
from sklearn.linear_model import LinearRegression
#simple linear regression
lr = LinearRegression()
X = df[['number_of_reviews']]
Y = df['price']
lr.fit(X, Y)
Yhat = lr.predict(X)
Yhat[0:5]
#in the form of y = a + bx
lr.intercept_
lr.coef_

#multiple regression
Z = df[['number_of_reviews', 'minimum_nights', 'availability_365']]
lr.fit(Z, df['price'])
Yhat = lr.predict(Z)
Yhat[0:5]
lr.intercept_
lr.coef_

#Model evaluation, refinement
df= df._get_numeric_data()
df.head()

#split data into training and testing sets
#I will use 20 percent of the data for testing
y_data = df['price']
x_data = df.drop('price', axis = 1)
from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test = train_test_split(x_data, y_data,test_size = 0.20,random_state = 1)
x_test.shape[0]
x_train.shape[0]
