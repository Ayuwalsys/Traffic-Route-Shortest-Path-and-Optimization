import pandas as pd

def read_data_from_file(file_path):
    #function read file using pandas dataFrame
    data = pd.read_csv(file_path)
    data = data.rename(columns={"X": "X1", "Y": "Y1"})
    data['X2'] = data['X1'].shift(-1)
    data['Y2'] = data['Y1'].shift(-1)
    data['Dist'] = data.apply(lambda row: ((row['X2'] - row['X1'])**2 + (row['Y2'] - row['Y1'])**2) ** 0.5, axis=1)
    data = data.dropna()
    return data