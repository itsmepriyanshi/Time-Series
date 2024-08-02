import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    return data

def prepare_univariate_data(data):
    return data.iloc[:-2, 0:2]

def prepare_bivariate_data(data):
    return data.iloc[0:-2, 0:3]