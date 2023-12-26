# src/utils.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def load_model(model_path):
    """
    Load a trained machine learning model from the given file path.

    Parameters:
    - model_path (str): The file path of the saved model.

    Returns:
    - model: The loaded machine learning model.
    """
    try:
        model = pickle.load(open(model_path, 'rb'))
        return model
    except Exception as e:
        raise ValueError(f"Failed to load the model from {model_path}. Error: {e}")



def load_and_split_data():
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_random_forest(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model
