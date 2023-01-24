import math

def solution(n):
    
    tmp = int(n**(0.5))
    if tmp**2 == n:
        return (tmp+1)**2
    else:
        return -1