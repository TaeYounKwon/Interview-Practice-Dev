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

def solution2(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)