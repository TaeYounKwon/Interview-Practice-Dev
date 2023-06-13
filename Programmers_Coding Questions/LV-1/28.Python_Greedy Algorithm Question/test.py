# https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(n, lost, reserve):
    answer = 0
    new_lost = list(set(lost)-set(reserve))
    new_reserve = list(set(reserve) - set(lost))
    
    if len(lost)==0:
        return n
    
    for i in range(1,n+1):    
        if i not in new_lost:
            answer+=1
        else:
            if i-1 in new_reserve:
                new_reserve.remove(i-1)
                answer+=1
            elif i+1 in new_reserve:
                new_reserve.remove(i+1)
                answer+=1
            
                
    return answer