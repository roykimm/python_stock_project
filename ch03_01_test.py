import numpy as np

A = np.array([[1,2],[3,4]])

print(A)
print(A.ndim)
print(A.shape)
print(A.dtype)
print(A.max(), A.mean(), A.min(), A.sum())
print(A.T)  # 전치
print(A.flatten())  # 평탄화
print(A + A)
print(A/A)

B = np.array([10,100])

print(A*B)  # 브로드캐스팅 B 행렬을 A 행렬과 사이즈를 맞춰줌

# 내적 구하기 
# 행렬 A가 m x k 행렬이고 , 행렬 B가 k X n 일때
# 행렬 A와 행렬 B를 곱한 행렬 C는 m X n 의 사이즈를 가진다. 
# 행렬 C의 i행 j열에 해당하는 원소를 행렬 A의 i행과 행렬B 의 내적이라고 한다.

# 넘파이에서는 벡터를 1차원 배열로, 행렬을 2차원 배열로 처리한다.
# 넘파이에서 배열끼리 곱셈 연산을 할때 기본적으로 원소별 연산을 수행하기 때문에 두배열의 내적 곱을 
# 구하려면 dot() 함수를 사용 해야 한다.
# 스칼라, 

print(B.dot(B))
