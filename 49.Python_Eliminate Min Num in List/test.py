import math

def solution(arr):
    answer = []
    if len(arr)==0 or len(arr)==1:
        return [-1]
    
    mnumb = math.inf
    for i in arr:
        if mnumb>i:
            mnumb=i
            
    arr.remove(mnumb)
    answer = arr
    
    return answer

#방법 2
def rm_small(mylist):
    # 함수를 완성하세요
    return [i for i in mylist if i > min(mylist)]