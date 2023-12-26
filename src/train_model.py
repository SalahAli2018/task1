import argparse
from utils import load_and_split_data, train_random_forest
import pickle
def train_model(model_path):
    X_train, _, y_train, _ = load_and_split_data()
    model = train_random_forest(X_train, y_train)

    # Save the trained model (you can customize this part based on your needs)
    pickle.dump(model, open(model_path, 'wb'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a Random Forest model on the iris dataset.")
    parser.add_argument("--model_path", type=str, required=True, help="Path to model_path")
    args = parser.parse_args()
    train_model(args.model_path)
