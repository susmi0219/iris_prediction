from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib

iris = load_iris()
print(iris.data)
print(iris.target)
print(iris.feature_names)
print(iris.target_names)
X=iris.data
Y=iris.target

X_train,X_test,y_train,y_test = train_test_split(
test_size = 0.2,
random_state = 42,

)
model.fit()


