# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def interpret(dr):
    bonus = ['S','D','T','#','*']
    tmp = ''
    tmp2 = ''
    score = []
    option = []
    for i in range(len(dr)):
        
        if dr[i] not in bonus:
            tmp+=dr[i]
            if tmp2 != '':
                option.append(tmp2)
                tmp2 = ''
        else:
            tmp2+=dr[i]
            
            if tmp != '':
                score.append(tmp)
                tmp = ''
            if i == len(dr)-1:
                option.append(tmp2)
    return score, option

def solution(dr):
    answer = 0
    s, b = interpret(dr)
    score = []
    tmp = 0
    star = False
    for i in range(len(s)):
        tmp = int(s[i])
        for j in range(len(b[i])):    
            if b[i][j]=='D':
                tmp=tmp**2
            elif b[i][j]=='T':
                tmp = tmp**3
            elif b[i][j]=='*':
                tmp *=2
                if len(score) != 0:
                    score[-1] *= 2 
            elif b[i][j]=='#':
                tmp *= (-1)
            else:
                pass
        score.append(tmp)
    answer = sum(score)
    return answer