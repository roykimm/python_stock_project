# 시리즈 생성

import pandas as pd
s = pd.Series([0.0,3.6,2.0,5.8,4.2,8.0])


s.index = pd.Index([0.0,1.2,1.8,3.0,3.6,4.8])
s.index.name = 'my_index'
s.name = 'my_series'

s[5.8] = 5.5     # 추가시 방법
print(s)