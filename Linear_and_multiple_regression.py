#First, without training and testing data
#simple linear regression
from sklearn.linear_model import LinearRegression
#simple linear regression
lr = LinearRegression()
X = df[['number_of_reviews']]
Y = df['price']
lr.fit(X, Y)
predicted_price = lr.predict(X)
predicted_price[0:5]
#in the form of y = a + bx
lr.intercept_
lr.coef_

#multiple regression
Z = df[['number_of_reviews', 'minimum_nights', 'availability_365']]
lr.fit(Z, df['price'])
predicted_price = lr.predict(Z)
predicted_price[0:5]
lr.intercept_
lr.coef_

#Model evaluation, refinement
df= df._get_numeric_data()
df.head()

#split data into training and testing sets
#I will use 20 percent of the data for testing
lm = LinearRegression()
y_data = df['price']
x_data = df.drop('price', axis = 1)
from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test = train_test_split(x_data, y_data,test_size = 0.20,random_state = 1)
x_test.shape[0]
x_train.shape[0]

#fitting and training the model
lm.fit(x_train[['number_of_reviews', 'minimum_nights',
                'availability_365', 'calculated_host_listings_count']], y_train)
predicted_price = lm.predict(x_test[['number_of_reviews', 'minimum_nights',
                'availability_365', 'calculated_host_listings_count']])

#comparing with actual values, the model does not perform very well in predicting prices
predicted_price[0:5]
#intercept and coefficients for our eqaution;
lm.intercept_
lm.coef_

#linear regression, using train and test data
y = df[['number_of_reviews', 'minimum_nights',
                'availability_365', 'calculated_host_listings_count', 'price']]

#number_of_reviews is the independent variable
msk = np.random.rand(len(df)) < 0.7
train = y[msk]
test = y[~msk]
lm
train_x = np.asarray(train[['number_of_reviews']])
train_y = np.asarray(train[['price']])
lm.fit(train_x, train_y)
lm.intercept_
lm.coef_

'''we can compute MSE, MAE and rsquared scores.MSE will help us know whether our model is fit
for use. We want to see how close the regression points are, to the line of best-fit'''
#MSE is generally small, meaning number_of_reviews is a good predictor of price
from sklearn.metrics import r2_score
test_x = np.asanyarray(test[['number_of_reviews']])
test_y = np.asanyarray(test[['price']])
test_y_ = lm.predict(test_x)

print("Mean Absolute Error is:",np.mean(np.absolute(test_y_ - test_y)))
print("Mean Squared Error is:" ,np.mean(test_y_ - test_y)**2)
print("r squared score is:" ,r2_score(test_y_, test_y))


