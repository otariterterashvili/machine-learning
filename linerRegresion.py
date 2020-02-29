import numpy as np

from sklearn.linear_model import LinearRegression

x = np.array([1, 2, 3, 5, 7, 9])

x = x.reshape(-1, 1)

y = np.array([3, 5, 7, 12, 17, 20])


model = LinearRegression()

model.fit(x, y)

ss = model.score(x, y)
y_pred = model.predict(x)

print(y_pred)

