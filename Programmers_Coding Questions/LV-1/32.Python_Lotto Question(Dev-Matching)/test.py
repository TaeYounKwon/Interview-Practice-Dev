# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    cnt = 0
    cnt_zero = 0
    prize = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    for numb in lottos:
        if numb in win_nums:
            cnt +=1
        elif numb == 0:
            cnt_zero +=1 
    
    max_match = cnt + cnt_zero
    min_match = cnt
    
    answer = [prize[max_match], prize[min_match]]
    
    
    return answer