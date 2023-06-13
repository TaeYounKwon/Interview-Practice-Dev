# https://school.programmers.co.kr/learn/courses/30/lessons/140108

import collections


def solution(x, y):
    answer=''
    x = collections.Counter(x)
    y = collections.Counter(y)
    
    cal = x - y
    if cal == x:
        return '-1'
    union = x-cal
    result = []
    for k, v in union.items():
        for i in range(0,v):
            result.append(k)

    result.sort(reverse=True)
    if result[0]=='0':
        return '0'
    for i in result:
        answer+=i
    return answer