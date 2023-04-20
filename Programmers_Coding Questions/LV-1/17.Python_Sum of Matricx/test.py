import numpy as np

def solution(arr1, arr2):
    a_list = np.array(arr1)
    b_list = np.array(arr2)
    result = a_list + b_list
    print(type(result))
    answer = result.tolist()
    print(type(answer))
    return answer

def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer