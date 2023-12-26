# src/predict_model.py
import argparse
import pandas as pd
import numpy as np 
from utils import load_and_split_data, load_model

def predict_model(input_values, input_path, output_path):
    # Load the trained model
    model = load_model(input_path)
    # Make predictions
    input_values=np.array(input_values).reshape(1,-1)
    predictions = model.predict(input_values)
    print(predictions)

    # Save predictions to the specified output path as a CSV file
    df = pd.DataFrame({'Prediction': predictions})
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make predictions using a trained model.")
    parser.add_argument('--input', nargs=4, type=int, help='Input values (exactly 4 integers)')
    parser.add_argument("--model_path", type=str, required=True, help="Path to the trained model")
    parser.add_argument("--output", type=str, required=True, help="Path to output CSV file")
    args = parser.parse_args()
    print(args.input)
    predict_model(args.input, args.model_path, args.output)
