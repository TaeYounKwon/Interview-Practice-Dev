def solution(s):
    
    if len(s) != 4 and len(s) !=6:
        return False
    
    
    try:
        tmp = int(s)
        return True
    except:
        return False
    
def alpha_string46(s):
    #함수를 완성하세요

    return s.isdigit() and len(s) in [4,6]