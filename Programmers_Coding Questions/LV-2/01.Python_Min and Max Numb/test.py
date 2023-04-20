def solution(s):
    answer = ''
    tmpString = s.split(' ')
    tmp = tmpString
    for i in range(len(tmpString)):
        tmp[i]=int(tmpString[i])
    numb_min = min(tmp)
    numb_max = max(tmp)
    answer = str(numb_min) +' '+ str(numb_max)
    return answer


def solution2(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))