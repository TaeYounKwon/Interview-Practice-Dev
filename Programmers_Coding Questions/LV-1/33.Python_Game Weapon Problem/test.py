# https://school.programmers.co.kr/learn/courses/30/lessons/136798

def divisor(numb): 
    cnt = 0
    for i in range(1, int(numb**(1/2))+1):
        if numb%i==0:
            cnt+=1
            if i < numb//i:
                cnt+=1
    return cnt

def solution(number, limit, power):
    answer = 0
    tmp = []
    
    for i in range(1,number+1):
        val = divisor(i)
        tmp.append(val)
    
    for i in tmp:
        if i<=limit:
            answer+=i
        else:
            answer+=power
    
    return answer