def solution(s):
    answer = ''
    s = s.split(" ")
    for i in range(len(s)):
        answer += s[i].capitalize() 
        if i != len(s)-1:
            answer += ' '

    return answer


def Jaden_Case(s):
    # 함수를 완성하세요
    return s.title()