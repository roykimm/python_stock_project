import pandas as pd

df = pd.DataFrame({
                    'KOSPI': [1915, 1961, 2026, 2467, 2041], 
                    'KOSDAQ': [542,682, 631, 798, 674]
                 },
                 index = [2014,2015,2016,2017,2018])

print(df)
print(df.describe())

for i in df.index:
    print(i, df['KOSPI'][i], df['KOSDAQ'][i])

for row in df.itertuples(name="KRX"):
    print(row)