import pandas as pd

s = pd.Series([1.2,2.3,4.5,8.0])
print(s)

s.index = pd.Index([1,3,5,7])
s.index.name = 'INDEX'
s.name = 'SERIES'




