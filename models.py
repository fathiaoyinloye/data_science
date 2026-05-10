
import pandas as pd
import matplotlib.pyplot as plt


housing_data = pd.read_csv('/home/omotemmy/Downloads/housing.csv')
print(housing_data.head())

def split_data(housing_data, targted_column, test_size=0.2, random_state=42):
    
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]