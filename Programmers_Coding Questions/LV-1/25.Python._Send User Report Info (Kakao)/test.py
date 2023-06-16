# https://school.programmers.co.kr/learn/courses/30/lessons/140108

from collections import deque

def solution(s):
    answer = 0
    queue = deque(s)
    
    a = queue.popleft()
    x, y = 1, 0
    while queue:
        b = queue.popleft()
        if a == b:
            x+=1
        else:
            y+=1
        if x==y:
            answer+=1
            x,y = 1, 0
            if len(queue) != 0:
                a = queue.popleft()
                b = ''
            if len(queue) == 0 and b == '':
                answer+=1
                break
    return answer