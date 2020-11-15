import pickle
from pandas import DataFrame

def predictor(data):
    filename = 'final_model.sav'
    read = open(filename, 'rb')
    model = pickle.load(read)
    df = DataFrame(data, index=[1])
    return model.predict_proba(df)

def get_unique(dataset, column):
    return sorted(dataset[column].unique().tolist())