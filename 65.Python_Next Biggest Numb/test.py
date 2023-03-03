def solution(n):
    tmp = n
    n_tmp = bin(n).count('1')
    
    while(True):
        tmp +=1
        tmp_check = bin(tmp).count('1')
        if n_tmp == tmp_check:
            return tmp
    