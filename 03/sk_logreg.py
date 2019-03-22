>>> import numpy as np
>>> from sklearn.linear_model import LogisticRegression
>>> X = np.array([[1, 0], [0, 1], [3, 2], [2, 3]])
>>> y = np.array([0, 0, 1, 1])
>>> reg = LogisticRegression(solver='lbfgs').fit(X, y)
>>> reg.score(X, y)
1.0
>>> reg.coef_
array([1., 2.])
>>> reg.intercept_ 
3.0000...
>>> reg.predict(np.array([[3, 5]]))
array([1])
