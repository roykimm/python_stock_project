# 시리즈 생성

import pandas as pd

s = pd.Series([1.2,1.3])
ser = pd.Series([1,2], index=[1.2,1.3])
s = s.append(ser)
print(s)

print(s.index[-1])
print(s.values[-1])
print(s.loc[0.0])   # 로케이션 인덱서 : index를 넘기고 값(value)을 받아온다.
print(s.values[:])

s.drop(1.3) # 시리즈의 원소를 삭제 하려면 drop()메서드의 인수로 삭제하고자 하는 원소의 인덱스 값을 넘겨줌
print(s)

print(s.describe())