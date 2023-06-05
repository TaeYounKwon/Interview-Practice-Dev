# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def count_skip(start,skip,add):
    cnt = 0
    while True:
        if start in skip:
            start+=1
        elif cnt!=add:
            start+=1
            cnt+=1
            
        if start>122:
            start-=26
            
        if cnt==add and start not in skip:
            break
            
    return start
    

def solution(w, s, index):
    answer = ''
    skip = []
    for i in s:
        tmp = ord(i)
        skip.append(tmp)
    skip.sort()
    
    for i in w:
        tmp = ord(i)
        val = count_skip(tmp,skip,index)
        tmp2 = chr(val)
        answer+=tmp2
        
        
    return answer