import pandas as pd

df = pd.read_csv('ford-mondeo_32_ofert.csv')

print(df[['price']].describe())