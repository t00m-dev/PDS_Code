import pandas as pd
import os
import pickle


def read_file(path=os.path.join(os.getcwd(), "data/input/IRIS.csv")):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print("Data file not found. Path was "+path)


def read_model():
    path = os.path.join(os.getcwd(), "data/output/model.pkl")
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model
