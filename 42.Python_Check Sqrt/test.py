import math

def solution(n):
    
    tmp = int(n**(0.5))
    if tmp**2 == n:
        return (tmp+1)**2
    else:
        return -1
    
# 방법 2     
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'