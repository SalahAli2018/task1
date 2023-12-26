from src.utils import load_and_split_data, train_random_forest
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import numpy as np

def test_load_and_split_data():
    iris = load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = load_and_split_data()

    assert X_train.shape[1] == X_test.shape[1] == X.shape[1]
    assert len(y_train) > 0
    assert len(y_test) > 0

def test_train_random_forest():
    X, _, y, _ = load_and_split_data()
    model = train_random_forest(X, y)

    # Check if the model is trained (basic check)
    assert isinstance(model, RandomForestClassifier)
    assert hasattr(model, 'predict')

    # Check if the model can make predictions on a dummy input
    dummy_input = np.zeros((1, X.shape[1]))
    prediction = model.predict(dummy_input)
    assert prediction.shape == (1,)
