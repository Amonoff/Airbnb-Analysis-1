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
