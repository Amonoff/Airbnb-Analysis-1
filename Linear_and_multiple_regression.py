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
