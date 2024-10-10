import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error

data = pd.read_excel('../dataset/dataCleaned.xlsx')

# split data into train and test with cross validation
X = data['Annee'].values.reshape(-1, 1)
y = data['Prix moyen au m²'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# train the model
model = LinearRegression()
model.fit(X_train, y_train)

# make predictions
y_pred = model.predict(X_test)

# evaluate the model
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
print('Accuracy:', model.score(X_test, y_test))
