# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    result = {
        'R':0,
        'T':0,
        'C':0,
        'F':0,
        'J':0,
        'M':0,
        'A':0,
        'N':0
    }
    
    for i in range(len(survey)):
        score = choices[i]
        letter_1 = survey[i][0]
        letter_2 = survey[i][1]
        if score < 4:
            result[letter_1] += 4-score
        elif score>4:
            result[letter_2] += score-4
        else:
            pass
    
    if result['R']>=result['T']:
        answer+='R'
    else:
        answer+='T'
    
    if result['C']>=result['F']:
        answer+='C'
    else:
        answer+='F'

    if result['J']>=result['M']:
        answer+='J'
    else:
        answer+='M'

    if result['A']>=result['N']:
        answer+='A'
    else:
        answer+='N'
    
    return answer