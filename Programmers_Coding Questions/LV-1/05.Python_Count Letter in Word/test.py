def solution(s):    
    return s.lower().count('p')==s.lower().count('y')

# 방법 2
def solution(s):
    answer = True
    p_cnt = 0
    y_cnt = 0
    for l in s:
        if l == 'p' or l=='P':
            p_cnt +=1
        elif l == 'y' or l=='Y':
            y_cnt +=1

    if p_cnt != y_cnt:
        answer=False


    return answer